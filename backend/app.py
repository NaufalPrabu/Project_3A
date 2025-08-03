import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import joblib
from flask_cors import CORS
from utils.feature_extraction import extract_features

# Inisialisasi Flask app
app = Flask(__name__)
CORS(app)  # Agar React dapat mengakses API Flask

# Folder untuk menyimpan gambar upload
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load model dan label encoder
model = joblib.load("svm_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

@app.route('/')
def index():
    return "API Deteksi Kesegaran Apel Aktif."

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'Tidak ada file yang dikirim'}), 400

    file = request.files['image']
    
    if file.filename == '':
        return jsonify({'error': 'Nama file kosong'}), 400

    try:
        # Simpan file ke folder upload
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        # Ekstraksi fitur gambar
        features = extract_features(file_path)
        if features is None:
            return jsonify({'error': 'Gagal membaca gambar'}), 500

        # Prediksi menggunakan model SVM
        pred_encoded = model.predict([features])[0]
        label = label_encoder.inverse_transform([pred_encoded])[0]

        # Langsung kirim hasil prediksi (freshapples atau rottenapples)
        result = label

        return jsonify({'result': result})

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({'error': 'Terjadi kesalahan saat memproses gambar'}), 500

if __name__ == '__main__':
    app.run(debug=True)
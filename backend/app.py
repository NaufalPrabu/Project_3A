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

# Allowed extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Load model SVM
model = joblib.load("svm_model.pkl")

@app.route('/')
def index():
    return "API Deteksi Kesegaran Apel Aktif."

@app.route('/predict', methods=['POST'])
def predict():
    # Pastikan ada file gambar dalam request
    if 'image' not in request.files:
        return jsonify({'error': 'Tidak ada file yang dikirim'}), 400

    file = request.files['image']
    
    if file.filename == '':
        return jsonify({'error': 'Nama file kosong'}), 400

    # Cek ekstensi file
    if not allowed_file(file.filename):
        return jsonify({'error': 'Format file tidak didukung. Gunakan gambar .jpg atau .png.'}), 400

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
        prediction = model.predict([features])[0]
        return jsonify({'result': prediction})

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({'error': 'Terjadi kesalahan saat memproses gambar'}), 500

if __name__ == '__main__':
    app.run(debug=True)

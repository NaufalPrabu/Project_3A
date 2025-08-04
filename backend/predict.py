import argparse
import joblib
import os
from utils.feature_extraction import extract_features

# Allowed extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Load model
model = joblib.load("svm_model.pkl")

# Argumen command-line
parser = argparse.ArgumentParser(description="Prediksi kesegaran apel dari gambar.")
parser.add_argument("--image", type=str, required=True, help="Path ke file gambar")
args = parser.parse_args()

# Validasi ekstensi file
if not allowed_file(args.image):
    print("Format file tidak didukung. Gunakan gambar .jpg atau .png.")
    exit(1)

# Ekstrak fitur dari gambar
features = extract_features(args.image)

# Prediksi
if features is not None:
    prediction = model.predict([features])[0]
    print(f"Hasil prediksi: {prediction}")
else:
    print("Gagal memproses gambar.")

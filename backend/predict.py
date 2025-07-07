import argparse
import joblib
from utils.feature_extraction import extract_features

# Load model
model = joblib.load("svm_model.pkl")

# Argumen command-line
parser = argparse.ArgumentParser(description="Prediksi kesegaran apel dari gambar.")
parser.add_argument("--image", type=str, required=True, help="Path ke file gambar")
args = parser.parse_args()

# Ekstrak fitur dari gambar
features = extract_features(args.image)

# Prediksi
if features is not None:
    prediction = model.predict([features])[0]
    print(f"Hasil prediksi: {prediction}")
else:
    print("Gagal memproses gambar.")

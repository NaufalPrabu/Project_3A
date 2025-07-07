# Aplikasi Deteksi Kesegaran Apel
Dibuat oleh: Naufal Prabu
Fitur: Ekstraksi LBP + Histogram Warna, Klasifikasi SVM

## Struktur Folder
├── app.py
├── model.py
├── predict.py
├── svm_model.pkl
├── utils/
│   ├── preprocessing.py
│   └── feature_extraction.py
├── dataset/
│   ├── train/
│   └── test/
├── uploads/
├── requirements.txt
└── README.txt

## Cara Menjalankan
1. Install dependensi:
   pip install -r requirements.txt

2. Latih model (jika belum):
   python model.py

3. Jalankan Flask API:
   python app.py

4. Prediksi manual (opsional):
   python predict.py --image path/to/image.jpg

## Akses Web API
- Endpoint: POST http://localhost:5000/predict
- Form field: 'file' = gambar apel
- Response: {"prediction": "freshapples"} atau {"prediction": "rottenapples"}
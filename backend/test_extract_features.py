from utils.feature_extraction import extract_features  # sesuaikan path modul

# Path ke gambar uji
image_path = "dataset/test/freshapples/r0_3.jpg"

# Jalankan ekstraksi fitur
fitur = extract_features(image_path)

# Cek keberhasilan
if fitur is not None:
    print(f"\n[SUKSES] Ekstraksi fitur berhasil. Panjang fitur: {len(fitur)}")
else:
    print("[GAGAL] Gambar tidak berhasil diproses.")

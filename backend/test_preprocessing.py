from utils.preprocessing import preprocess_image

# Path gambar uji coba
image_path = "dataset/test/rottenapples/saltandpepper_Screen Shot 2018-06-07 at 2.16.18 PM.png"

# Jalankan fungsi preprocessing
hasil = preprocess_image(image_path, debug=True)

# Tampilkan status
if hasil is not None:
    print("[SUKSES] Preprocessing berhasil dilakukan.")
else:
    print("[GAGAL] Tidak berhasil memproses gambar.")
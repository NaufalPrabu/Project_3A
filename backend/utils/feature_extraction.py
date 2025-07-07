import cv2
import numpy as np
from skimage.feature import local_binary_pattern

def extract_features(image_path):
    print(f"[DEBUG] Membaca gambar dari: {image_path}")
    
    # Baca gambar
    image = cv2.imread(image_path)
    if image is None:
        print("[ERROR] Gagal membaca gambar! Pastikan path dan format file benar.")
        return None

    # Resize agar konsisten
    image = cv2.resize(image, (100, 100))

    # Konversi ke grayscale untuk LBP
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Ekstraksi fitur tekstur: LBP
    radius = 1
    n_points = 8 * radius
    lbp = local_binary_pattern(gray, n_points, radius, method="uniform")
    lbp_hist, _ = np.histogram(
        lbp.ravel(),
        bins=np.arange(0, n_points + 3),
        range=(0, n_points + 2)
    )
    lbp_hist = lbp_hist.astype("float")
    lbp_hist /= (lbp_hist.sum() + 1e-7)

    # Ekstraksi fitur warna: Histogram RGB
    chans = cv2.split(image)
    color_features = []
    for chan in chans:
        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        hist = cv2.normalize(hist, hist).flatten()
        color_features.extend(hist)

    fitur_akhir = np.hstack([lbp_hist, color_features])
    print(f"[DEBUG] Fitur berhasil diekstraksi. Panjang vektor fitur: {len(fitur_akhir)}")

    # Tambahan: tampilkan 15 nilai awal dari vektor fitur
    print(f"[HASIL] 15 nilai awal fitur: {np.round(fitur_akhir[:15], 4).tolist()}")

    return fitur_akhir

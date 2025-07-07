import cv2
import numpy as np

def preprocess_image(image_path, debug=True):
    # Baca gambar
    image = cv2.imread(image_path)
    if image is None:
        print("[ERROR] Gagal membaca gambar.")
        return None

    print(f"[INFO] Ukuran asli gambar: {image.shape}")

    # Resize
    image = cv2.resize(image, (100, 100))
    print(f"[INFO] Ukuran setelah resize: {image.shape}")

    if debug:
        cv2.imshow("Resized Image", image)
        cv2.waitKey(0)

    # Konversi ke grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print(f"[INFO] Gambar setelah konversi grayscale: {gray.shape}")

    if debug:
        cv2.imshow("Grayscale Image", gray)
        cv2.waitKey(0)

    # Normalisasi piksel grayscale (0–255 → 0.0–1.0)
    gray_normalized = gray.astype("float32") / 255.0

    # Ambil 3 piksel untuk ditampilkan hasil normalisasinya
    contoh_piksel = gray[0:3, 0]
    contoh_norm = gray_normalized[0:3, 0]
    print("[INFO] Contoh normalisasi piksel (sebelum → sesudah):")
    for before, after in zip(contoh_piksel, contoh_norm):
        print(f"        {before} → {round(after, 3)}")

    # Optional: Gaussian blur (jika ingin mengurangi noise)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    # Optional: Threshold (jika ingin konversi ke biner)
    _, binary = cv2.threshold(blurred, 128, 255, cv2.THRESH_BINARY)

    if debug:
        cv2.imshow("Binary Image", binary)
        cv2.waitKey(0)

    return gray_normalized  # atau return binary/blurred sesuai kebutuhan

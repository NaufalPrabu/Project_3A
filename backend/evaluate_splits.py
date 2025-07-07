import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from utils.feature_extraction import extract_features

# Path ke dataset
DATASET_PATH = 'dataset/train'

# Load fitur
X, y = [], []
for label in os.listdir(DATASET_PATH):
    folder = os.path.join(DATASET_PATH, label)
    for fname in os.listdir(folder):
        img_path = os.path.join(folder, fname)
        features = extract_features(img_path)
        if features is not None:
            X.append(features)
            y.append(label)

# Skema pembagian
split_ratios = [0.2, 0.3, 0.4]
split_labels = ['80:20', '70:30', '60:40']
accuracies = []

# Evaluasi tiap skema
for ratio in split_ratios:
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=ratio, random_state=42)
    model = svm.SVC(kernel='linear', probability=True)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_val)
    acc = accuracy_score(y_val, y_pred)
    accuracies.append(acc)
    print(f"\n[Split {int((1 - ratio)*100)}:{int(ratio*100)}] Akurasi: {acc:.2%} (Train: {len(X_train)} | Test: {len(X_val)})")

# Tabel Hasil Evaluasi
print("\n📊 TABEL EVALUASI AKURASI")
print("=======================================")
print("  Skema   |  Train  |  Test  | Akurasi ")
print("----------|---------|--------|---------")
for i, ratio in enumerate(split_ratios):
    train_count = int(len(X) * (1 - ratio))
    test_count = len(X) - train_count
    print(f" {split_labels[i]:>7} | {train_count:^7} | {test_count:^6} | {accuracies[i]:.2%}")
print("=======================================")

# Grafik Perbandingan Akurasi
plt.figure(figsize=(8, 5))
plt.plot(split_labels, accuracies, marker='o', color='green', linestyle='--')
plt.title("Perbandingan Akurasi Tiap Skema Split Data")
plt.xlabel("Skema Split")
plt.ylabel("Akurasi")
plt.ylim(0, 1)
plt.grid(True)
plt.savefig("evaluasi_split.png")
plt.show()

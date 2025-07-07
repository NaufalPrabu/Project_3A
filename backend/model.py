import os
import cv2
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
from utils.feature_extraction import extract_features

# Path ke dataset
DATASET_PATH = 'dataset/train'  # berisi freshapples/ dan rottenapples/

# Load data & ekstraksi fitur
X, y = [], []
for label in os.listdir(DATASET_PATH):
    folder = os.path.join(DATASET_PATH, label)
    for fname in os.listdir(folder):
        img_path = os.path.join(folder, fname)
        features = extract_features(img_path)
        if features is not None:
            X.append(features)
            y.append(label)

# Split data: 80% train, 20% val
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Latih model SVM
model = svm.SVC(kernel='linear', probability=True)
model.fit(X_train, y_train)

# Prediksi & Evaluasi
y_pred = model.predict(X_val)

# Akurasi
accuracy = accuracy_score(y_val, y_pred)
print(f"Akurasi model: {accuracy:.2%}")

# Confusion Matrix
cm = confusion_matrix(y_val, y_pred, labels=["freshapples", "rottenapples"])
print("\nConfusion Matrix:")
print(cm)

# Classification Report
report = classification_report(y_val, y_pred, target_names=["freshapples", "rottenapples"])
print("\nClassification Report:")
print(report)

# Simpan model
joblib.dump(model, 'svm_model.pkl')
print("Model disimpan ke 'svm_model.pkl'")

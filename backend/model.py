import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import joblib
from utils.feature_extraction import extract_features

# Path ke dataset
DATASET_PATH = 'dataset/train'  # Hanya folder freshapples dan rottenapples

# Load data & ekstraksi fitur
X, y = [], []
for label in os.listdir(DATASET_PATH):
    if label == 'notapple':
        continue  
    folder = os.path.join(DATASET_PATH, label)
    for fname in os.listdir(folder):
        img_path = os.path.join(folder, fname)
        features = extract_features(img_path)
        if features is not None:
            X.append(features)
            y.append(label)

# Encode label (freshapples, rottenapples)
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Split data dan train
X_train, X_val, y_train, y_val = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Latih model SVM
model = svm.SVC(kernel='linear', probability=True)
model.fit(X_train, y_train)

# Prediksi & Evaluasi
y_pred = model.predict(X_val)

# Akurasi
accuracy = accuracy_score(y_val, y_pred)
print(f"Akurasi model: {accuracy:.2%}")

# Decode label untuk laporan
y_val_decoded = le.inverse_transform(y_val)
y_pred_decoded = le.inverse_transform(y_pred)

# Confusion Matrix
cm_labels = le.classes_
cm = confusion_matrix(y_val_decoded, y_pred_decoded, labels=cm_labels)
print("\nConfusion Matrix:")
print(cm)

# Classification Report
report = classification_report(y_val_decoded, y_pred_decoded, target_names=cm_labels)
print("\nClassification Report:")
print(report)

# Visualisasi Confusion Matrix
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=cm_labels, yticklabels=cm_labels)
plt.title('Confusion Matrix')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.tight_layout()
plt.show()

# Simpan model & label encoder
joblib.dump(model, 'svm_model.pkl')
joblib.dump(le, 'label_encoder.pkl')
print("Model disimpan ke 'svm_model.pkl'")
print("Label encoder disimpan ke 'label_encoder.pkl'")

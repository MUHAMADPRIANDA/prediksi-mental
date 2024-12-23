import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Memuat dataset
df = pd.read_csv("prediksi_mental_siswa.csv")

# Pisahkan fitur dan label
X = df[["Durasi_Belajar", "Skor_Latihan", "Waktu_Istirahat"]]
y = df["Label"]

# Membagi data menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Membuat model RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Melatih model
model.fit(X_train, y_train)

# Melakukan prediksi
y_pred = model.predict(X_test)

# Mengevaluasi model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Menyimpan model
joblib.dump(model, "prediksi_mental_siswa_model_v1.pkl")

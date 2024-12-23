from flask import Flask, request, jsonify
import joblib
from flask_cors import CORS  # Import CORS

# Inisialisasi Flask app
app = Flask(__name__)

# Mengaktifkan CORS untuk aplikasi ini
CORS(app)  # Membolehkan permintaan dari semua domain

# Memuat model yang telah dilatih
model_path = "prediksi_mental_siswa_model_v1.pkl"
model = joblib.load(model_path)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Ambil data dari request
        data = request.get_json()

        # Validasi input
        durasi_belajar = data.get("Durasi_Belajar")
        skor_latihan = data.get("Skor_Latihan")
        waktu_istirahat = data.get("Waktu_Istirahat")

        if None in (durasi_belajar, skor_latihan, waktu_istirahat):
            return jsonify({"error": "Invalid input data"}), 400

        # Format data untuk model
        input_data = [[durasi_belajar, skor_latihan, waktu_istirahat]]

        # Prediksi dengan model
        prediction = model.predict(input_data)[0]

        # Kirim hasil prediksi
        return jsonify({"prediksi": int(prediction)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Menjalankan server
if __name__ == "__main__":
    app.run(debug=True)

# Gunakan image dasar Python
FROM python:3.9-slim

# Set direktori kerja di dalam container
WORKDIR /app

# Salin file requirements.txt ke dalam container
COPY requirements.txt .

# Install dependensi
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh kode aplikasi ke dalam container
COPY . .

# Expose port untuk Flask (Flask secara default berjalan di port 5000)
EXPOSE 5000

# Perintah untuk menjalankan Flask
CMD ["python", "app.py"]

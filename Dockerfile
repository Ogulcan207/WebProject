# Python 3.11 tabanlı resmi imajı kullan
FROM python:3.11

# Terminal çıktılarını tamponlamadan göster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Çalışma dizinini oluştur
WORKDIR /app

# Sistem bağımlılıklarını yükle (MySQL için gerekli)
RUN apt-get update && apt-get install -y \
    libmariadb-dev gcc \
    && apt-get clean

# Gereksinimleri kopyala ve yükle
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Projeyi konteynıra kopyala
COPY . /app/

# Django geliştirme sunucusunu başlat
CMD ["python", "webproje/manage.py", "runserver", "0.0.0.0:8000"]

COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

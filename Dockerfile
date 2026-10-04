FROM python:3.12-slim

WORKDIR /app

# Python kesh va buferlashni o'chirish
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Kutubxonalarni o'rnatish
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Loyiha fayllarini nusxalash
COPY . .

# Botni ishga tushirish
CMD ["python", "bot.py"]

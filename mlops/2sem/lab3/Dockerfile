# Используем официальный образ Python в качестве базового
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы в контейнер
COPY main.py ./
COPY api.py ./
COPY requirements.txt ./

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Обучаем модель и сохраняем её
RUN python main.py

# Открываем порт для FastAPI приложения
EXPOSE 8000

# Запускаем FastAPI приложение с помощью uvicorn
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements-dev.txt .
RUN pip install --no-cache-dir -r requirements-dev.txt

COPY . .
WORKDIR /src

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
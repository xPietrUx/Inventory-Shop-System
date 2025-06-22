FROM python:3.13

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "inventory_shop_system.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
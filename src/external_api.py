# src/external_api.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные из .env

EXCHANGE_API_KEY = os.getenv('EXCHANGE_API_KEY')

def convert_to_rub(transaction):
    """
    Конвертирует сумму транзакции в рубли, если валюта USD или EUR.
    Для конвертации используется внешнее API для получения курса валют.
    """
    if transaction["currency"] not in ["USD", "EUR"]:
        return transaction["amount"]

    url = f"https://api.apilayer.com/exchangerates_data/convert"
    params = {
        "to": "RUB",
        "from": transaction["currency"],
        "amount": transaction["amount"]
    }
    headers = {
        "apikey": EXCHANGE_API_KEY
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data["result"]
    else:
        return transaction["amount"]

# src/external_api.py
import os
import requests
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

API_KEY = os.getenv('EXCHANGE_API_KEY')
API_URL = 'https://api.apilayer.com/exchangerates_data/convert'

def convert_to_rub(transaction):
    """
    Конвертирует сумму транзакции в рубли, если валюта транзакции USD или EUR.

    :param transaction: Словарь с данными о транзакции.
    :return: Сумма транзакции в рублях.
    """
    amount = transaction.get('amount', 0.0)
    currency = transaction.get('currency', '').upper()

    if currency not in ['USD', 'EUR']:
        return amount

    params = {
        'from': currency,
        'to': 'RUB',
        'amount': amount
    }

    headers = {
        'apikey': API_KEY
    }

    try:
        response = requests.get(API_URL, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get('result', 0.0)
    except requests.RequestException:
        return amount

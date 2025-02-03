import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv()


def load_and_clean_data(file_path):
    """Load && CSV data"""

    df = pd.read_csv(file_path)

    df["category"] = df["category"].str.lower().str.strip()

    df["our_price"] = df["our_price"].astype(str).str.replace("$", "", regex=False)
    df["our_price"] = pd.to_numeric(df["our_price"], errors="coerce")

    df["current_stock"] = pd.to_numeric(df["current_stock"], errors="coerce").fillna(0)

    return df


def get_exchange_rate(target_currency="EUR"):
    """Gets the exchange rate from USD to target_currency from Exchange Rate API."""
    API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")
    BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"
    
    if not API_KEY:
        raise ValueError("API Key no encontrada. Asegúrate de configurar el archivo .env.")
    
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        data = response.json()
        return data["conversion_rates"].get(target_currency, None)
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener la tasa de cambio: {e}")
        return None
    except ValueError as e:
        print(f"Error al procesar la respuesta de la API: {e}")
        return None

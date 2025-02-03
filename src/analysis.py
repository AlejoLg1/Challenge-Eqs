from utils import load_and_clean_data, get_exchange_rate

if __name__ == "__main__":
    import sys

    file_path = sys.argv[1] if len(sys.argv) > 1 else "data/products.csv"
    df = load_and_clean_data(file_path)

    target_currency = "EUR" # Example 
    exchange_rate = get_exchange_rate(target_currency)

    if exchange_rate:
        df["converted_price"] = df["our_price"] * exchange_rate
        print(f"Precios convertidos a {target_currency}:")
        print(df[["product_name", "our_price", "converted_price"]])

        df.to_csv("data/converted_prices.csv", index=False)
        print("Archivo guardado en data/converted_prices.csv")
    else:
        print("No se pudo obtener la tasa de cambio.")

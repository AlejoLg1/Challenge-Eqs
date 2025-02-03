from utils import load_and_clean_data, get_exchange_rate

if __name__ == "__main__":
    import sys

    file_path = sys.argv[1] if len(sys.argv) > 1 else "data/products.csv"
    df = load_and_clean_data(file_path)

    target_currency = "EUR"
    exchange_rate = get_exchange_rate(target_currency)

    if exchange_rate:
        df["converted_price"] = df["our_price"] * exchange_rate
        print(f"Prices converted to {target_currency}:")
        print(df[["product_name", "our_price", "converted_price"]])

        df.to_csv("data/converted_prices.csv", index=False)
        print("File saved: data/converted_prices.csv")
    else:
        print("⚠️ Could not retrieve exchange rate. Proceeding without conversion.")

    df["priority"] = df["current_stock"] - df["restock_threshold"]

    df["status"] = df["priority"].apply(lambda x: "⚠️" if x < 0 else "🟢")

    restock_df = df[df["priority"] < 0].sort_values(by="priority")

    if not restock_df.empty:
        print("\n🔍 Products needing restock:")
        print(restock_df[["product_name", "current_stock", "restock_threshold", "priority", "status"]])

        restock_df.to_csv("data/restock_analysis.csv", index=False)
        print("File saved: data/restock_analysis.csv")
    else:
        print("\n✅ No products require restocking.")

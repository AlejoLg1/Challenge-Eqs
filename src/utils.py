import pandas as pd

def load_and_clean_data(file_path):
    """Load && CSV data"""

    df = pd.read_csv(file_path)

    df["category"] = df["category"].str.lower().str.strip()

    df["our_price"] = df["our_price"].astype(str).str.replace("$", "", regex=False)
    df["our_price"] = pd.to_numeric(df["our_price"], errors="coerce")

    df["current_stock"] = pd.to_numeric(df["current_stock"], errors="coerce").fillna(0)

    return df

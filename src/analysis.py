from utils import load_and_clean_data

if __name__ == "__main__":
    import sys

    file_path = sys.argv[1] if len(sys.argv) > 1 else "data/products.csv"
    df = load_and_clean_data(file_path)
    
    print("Datos después de limpieza:")
    print(df.head())

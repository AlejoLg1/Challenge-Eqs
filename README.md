# 🛠️ 10EQS Data Integration Challenge

This project helps a small business owner **track product pricing against market conditions** by:
1. **Reading and processing product data** from a CSV file.
2. **Integrating an external data source** (Exchange Rate API) to convert prices.
3. **Generating actionable insights** by identifying products that need restocking.

---

## 📌 Features
- ✅ **Reads and cleans product data** from `products.csv`.
- ✅ **Converts prices** from USD to a target currency using Exchange Rate API.
- ✅ **Identifies products that need restocking** based on current stock vs. restock threshold.
- ✅ **Outputs insights** in `converted_prices.csv` and `restock_analysis.csv`.

---

## 📂 Repository Structure

```
├── README.md                 # Project documentation
├── .env.example              # API key configuration
├── data/
│   ├── products.csv          # Input data file
│   ├── converted_prices.csv  # Output: Converted prices
│   ├── restock_analysis.csv  # Output: Restock insights
├── src/
│   ├── analysis.py           # Main script
│   ├── utils.py              # Helper functions
├── requirements.txt          # Dependencies
└── report.md                 # Data insights report
```

---

## 🔧 Setup Instructions

### **1️⃣ Install Dependencies**
Ensure you have Python **3.8+** installed. Then, install the required packages:

```bash
pip install -r requirements.txt
```

---

### **2️⃣ Configure Environment Variables**
1. **Create a `.env` file** in the project root (or rename `.env.example` to `.env`).
2. Add your **Exchange Rate API Key**:

```
EXCHANGE_RATE_API_KEY=your_api_key_here
```

---

### **3️⃣ Run the Script**
The script accepts the CSV file path as an argument:

```bash
python src/analysis.py data/products.csv
```

If successful, it will generate:
- **`data/converted_prices.csv`** → Prices converted to the selected currency.
- **`data/restock_analysis.csv`** → Products that need restocking based on inventory levels.

---

## 📊 Insights Generated

### 📌 **Price Conversion**
The script converts product prices from USD to the selected currency (default: EUR) using real-time exchange rates.

### 📌 **Stock vs. Restock Analysis**
Identifies products that are **below their restock threshold** and prioritizes restocking by urgency.

| Product | Current Stock | Threshold | Priority | Status |
|---------|--------------|-----------|----------|--------|
| Yerba Mate | 5 | 10 | -5 | ⚠️ |
| Matcha Green Tea | 8 | 10 | -2 | ⚠️ |

---

## 🚀 Future Improvements
- **Support for additional external APIs** (e.g., competitor pricing for comparison).
- **Visualization of stock trends** to predict restocking needs.
- **Automated alerts** for low-stock products via email or dashboard.

---

## ⚠️ Known Issues & Limitations
- If the API request fails, the script **skips price conversion** and proceeds with stock analysis.
- The CSV file must have correct column names (`our_price`, `current_stock`, etc.).
- The script currently supports only **one target currency** at a time.

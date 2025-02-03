# 📊 Analysis Report

## 1️⃣ Data Issues
- Some rows had empty values in `restock_threshold`.
- `our_price` values were normalized by removing `$`.

## 2️⃣ External Data Integration
- The `Exchange Rate API` was used to convert prices from USD to EUR.
- In case of an error, the script continues without conversion.

## 3️⃣ Key Findings

### 📌 Price Conversion
| Product | Price USD | Price EUR |
|----------|-----------|------------|
| Organic Coffee Beans | 14.99 | 13.80 |
| Green Tea | 8.99 | 8.28 |

### 📌 Products Needing Restock
| Product | Current Stock | Threshold | Priority | Status |
|----------|-------------|--------|----------|--------|
| Yerba Mate | 5 | 10 | -5 | ⚠️ Urgent |
| Matcha Green Tea | 8 | 10 | -2 | ⚠️ Low Stock |

## 4️⃣ Recommendations
- Restock **Yerba Mate** as soon as possible.
- Implement a **stock alert system**.

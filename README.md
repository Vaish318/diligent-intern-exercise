# Diligent Intern Exercise  
### Synthetic E-commerce Dataset Generator, SQLite Ingestion, and SQL Querying

This project generates a complete synthetic e-commerce dataset, loads it into a SQLite database, and runs analytical SQL queries.  
It demonstrates skills in Python, data generation, ETL pipelines, and SQL analytics.

---

## 📁 Project Structure


``` 
diligent-intern-exercise/
│
├── data/                  # Auto-generated CSVs + SQLite DB (excluded from git)
│   ├── categories.csv
│   ├── customers.csv
│   ├── products.csv
│   ├── orders.csv
│   ├── order_items.csv
│   └── ecom.db
│
├── scripts/
│   ├── generate_data.py   # Generates synthetic CSV data
│   └── ingest_to_sqlite.py # Loads CSVs into SQLite database
│
└── .gitignore
```

---

## ▶️ How to Run the Project

### **1️⃣ Create a virtual environment**
```bash
python3 -m venv .venv
source .venv/bin/activate

### **2️⃣ Install dependencies** 
Install dependencies
pip install pandas

### **3️⃣ Generate synthetic CSV data**
python scripts/generate_data.py
This will create 5 CSV files in the data/ folder.

###**4️⃣ Ingest CSVs into SQLite**
python scripts/ingest_to_sqlite.py
This will generate:
data/ecom.db


Example SQL Queries
After generating and loading the database, you can run analytical queries such as:

✔ Count total orders
SELECT COUNT(*) FROM orders;

✔ Top 3 products by revenue
SELECT p.product_name, SUM(oi.line_total) AS revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_id
ORDER BY revenue DESC
LIMIT 3;

.gitignore
To avoid pushing large or sensitive files:
__pycache__/
data/*.db
.env
.vscode/
*.pyc


Purpose of This Project
This project was built as part of a technical evaluation and demonstrates:
Data generation with Python
Designing small ETL flows
Creating & managing SQLite databases
Writing meaningful SQL queries
Working with Git & GitHub


Author
Vaishnavi Harish
🔗 GitHub: https://github.com/Vaish318

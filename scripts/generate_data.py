# scripts/generate_data.py
import random
from datetime import datetime, timedelta
import pandas as pd
import os

os.makedirs("data", exist_ok=True)
random.seed(42)

# categories
categories = [
    {"category_id": 1, "category_name": "Apparel"},
    {"category_id": 2, "category_name": "Electronics"},
    {"category_id": 3, "category_name": "Home"},
    {"category_id": 4, "category_name": "Outdoor"},
    {"category_id": 5, "category_name": "Beauty"}
]
pd.DataFrame(categories).to_csv("data/categories.csv", index=False)

# products
product_names = [
    "Thermal Jacket", "Bluetooth Headphones", "Coffee Maker",
    "Camping Tent", "Face Moisturizer", "Trail Running Shoes",
    "Wireless Charger", "Desk Lamp", "Sunglasses", "Backpack"
]
products = []
for i, name in enumerate(product_names, start=1):
    cat_id = random.choice(categories)["category_id"]
    price = round(random.uniform(15, 350), 2)
    products.append({
        "product_id": i,
        "product_name": name,
        "category_id": cat_id,
        "price": price,
        "stock": random.randint(10, 500)
    })
pd.DataFrame(products).to_csv("data/products.csv", index=False)

# customers
first_names = ["Asha","Rahul","Priya","Vikas","Neha","Karan","Sonal","Rohit","Anita","Sandeep"]
last_names = ["Sharma","Patel","Kumar","Reddy","Mehra","Singh","Gupta","Nair","Das","Bose"]
customers = []
for i in range(1, 31):  # 30 customers
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    email = name.replace(" ", ".").lower() + f"{i}@example.com"
    customers.append({
        "customer_id": i,
        "name": name,
        "email": email,
        "join_date": (datetime.now() - timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d")
    })
pd.DataFrame(customers).to_csv("data/customers.csv", index=False)

# orders & order_items
orders = []
order_items = []
order_id = 1
for _ in range(1, 101):  # 100 orders
    cust = random.choice(customers)
    order_date = datetime.now() - timedelta(days=random.randint(0, 180))
    status = random.choices(["completed","cancelled","returned"], weights=[0.8,0.1,0.1])[0]
    orders.append({
        "order_id": order_id,
        "customer_id": cust["customer_id"],
        "order_date": order_date.strftime("%Y-%m-%d"),
        "status": status,
        "total_amount": 0.0
    })
    num_items = random.randint(1,4)
    total = 0.0
    for _ in range(num_items):
        prod = random.choice(products)
        qty = random.randint(1,3)
        price = prod["price"]
        line_total = round(price * qty, 2)
        total += line_total
        order_items.append({
            "order_id": order_id,
            "product_id": prod["product_id"],
            "quantity": qty,
            "unit_price": price,
            "line_total": round(line_total, 2)
        })
    orders[-1]["total_amount"] = round(total,2)
    order_id += 1

pd.DataFrame(orders).to_csv("data/orders.csv", index=False)
pd.DataFrame(order_items).to_csv("data/order_items.csv", index=False)

print("Generated CSV files.")

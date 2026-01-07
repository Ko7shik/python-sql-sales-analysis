import sqlite3
import pandas as pd

# Load CSV into SQLite
conn = sqlite3.connect(":memory:")
df = pd.read_csv("sales_data.csv")

df.to_sql("sales_data", conn, index=False, if_exists="replace")

# Run SQL queries
queries = {
    "Total Revenue": """
        SELECT SUM(quantity * price) AS total_revenue
        FROM sales_data
    """,

    "Revenue by Product": """
        SELECT product, SUM(quantity * price) AS revenue
        FROM sales_data
        GROUP BY product
        ORDER BY revenue DESC
    """,

    "Revenue by Region": """
        SELECT region, SUM(quantity * price) AS revenue
        FROM sales_data
        GROUP BY region
        ORDER BY revenue DESC
    """
}

for title, query in queries.items():
    print(f"\n--- {title} ---")
    result = pd.read_sql(query, conn)
    print(result)
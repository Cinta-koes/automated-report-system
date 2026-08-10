import sqlite3
import pandas as pd

def weekly_sales_summary():
    # Connect to the SQLite database
    conn = sqlite3.connect('sales.db')
    
    # Query to get weekly sales summary
    query = """
    SELECT Region, Category, ROUND(SUM(Sales), 2) as total_sales FROM sales
    GROUP BY Region, Category
    ORDER BY Region, Total_sales DESC
    """
    
    # Execute the query and load the results into a DataFrame
    df = pd.read_sql_query(query, conn)
    
    # Close the database connection
    conn.close()
    
    return df


def delayed_shipment_alert():
    # Connect to the SQLite database
    conn = sqlite3.connect('sales.db')
    
    # Query to get delayed shipments
    query = """
    SELECT 
            `Order ID`,
            `Order Date`,
            `Ship Date`,
            `Ship Mode`,
            `Customer Name`,
            City,
            State,
            julianday(`Ship Date`) - julianday(`Order Date`) as Days_To_Ship
        FROM sales
        WHERE julianday(`Ship Date`) - julianday(`Order Date`) > 7
        ORDER BY Days_To_Ship DESC
    """
    
    # Execute the query and load the results into a DataFrame
    df = pd.read_sql_query(query, conn)
    
    # Close the database connection
    conn.close()
    
    return df


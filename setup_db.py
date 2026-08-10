import pandas as pd
import sqlite3

df = pd.read_csv('data/train.csv', encoding='latin1')  # Replace 'data.csv' with your actual CSV file path
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y')
conn = sqlite3.connect('sales.db')  # Create a connection to the SQLite database
df.to_sql('sales', conn, if_exists='replace', index=False)  # Write the DataFrame to the database
conn.close()  # Close the database connection

print("Database setup complete. Data has been loaded into 'sales.db'.")
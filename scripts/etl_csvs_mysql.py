# script to extract data from multiple csvs and load them into a database

# Import packages
from sqlalchemy import create_engine, text

# Import parameters from config file
from config import csv_dir, db_name, db_host, db_pwd, db_user
import pandas as pd
from extract import extract_csvs
import time

start_time = time.time()

# Database connection details
user = db_user
password = db_pwd
host = db_host
database = db_name

# Create function for connecting to database and executing statements using with statement?

# Construct the connection string
connection_string = f"mysql+pymysql://{user}:{password}@{host}/{database}"

# Create the engine
engine = create_engine(connection_string)

# Print a message to confirm connection
print('Connected to MySQL database successfully!')

# Assign target table
target_table = 'holdings'

# Truncate table if it exists
with engine.connect() as conn:
    stmt = text(f"TRUNCATE TABLE {target_table}")
    conn.execute(stmt)
    print(f"Truncated table {target_table} succesfully")

# Print message for looping through data
print('Looping through directory of CSVs to ETL into database')

# Extract csvs to dataframe
df = extract_csvs(csv_dir)

# Remove comma in shares column
df['shares'] = df['shares'].str.replace(',', '')

# Clean up dollar amount column
df['market value ($)'] = df['market value ($)'].str.replace('$', '').str.replace(',', '')

# Clean up percentage column
df['weight (%)'] = df['weight (%)'].str.replace('%', '')

# Rename columns
df = df.rename(columns={'market value ($)':'total_value', 'weight (%)':'portfolio_percentage'})

# Set correct data types of columns
df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y')
df['shares'] = pd.to_numeric(df['shares'], errors='coerce')
df['total_value'] = pd.to_numeric(df['total_value'], errors='coerce')
df['portfolio_percentage'] = pd.to_numeric(df['portfolio_percentage'], errors='coerce')

# Insert data into the database table
df.to_sql(target_table, engine, index=False, if_exists='append')

# Close the engine (optional)
engine.dispose()

# Print message to confirm disconnection
print('Disconnected from database')

end_time = time.time()

total_time = end_time - start_time

print(f"Script execution time: {total_time} seconds")

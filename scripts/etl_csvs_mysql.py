# script to extract data from multiple csvs and return one dataframe

# Import packages
from sqlalchemy import create_engine

# Import parameters from config file
from config import csv_dir, db_name, db_host, db_pwd, db_user
import pandas as pd
import os

# Database connection details
user = db_user
password = db_pwd
host = db_host
database = db_name

# Construct the connection string
connection_string = f"mysql+pymysql://{user}:{password}@{host}/{database}"

# Create the engine
engine = create_engine(connection_string)

# Print a message to confirm connection
print('Connected to MySQL database successfully!')

# Loop through directory to extract data from csvs
for filename in os.listdir(csv_dir):
    
    # Check if it's a csv file
    if filename.endswith('.csv'):
    
        # Construct full path for csv
        file_path = os.path.join(csv_dir, filename)
        
        # Read csv as dataframe
        df = pd.read_csv(file_path)

        # Drop last row
        df = df[:-1]

        # Insert data into the database table
        df.to_sql('funds', engine, index=False, if_exists='append')

# Close the engine (optional)
engine.dispose()

# Print message to confirm disconnection
print('Disconnected from database')
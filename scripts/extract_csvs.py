# script to extract data from multiple csvs and return one dataframe

# Import packages
from sqlalchemy import create_engine

# Import parameters from config file
from config import csv_dir, db_name, db_host, db_pwd, db_user

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
print("Connected to MySQL database successfully!")

# Close the engine (optional)
engine.dispose()

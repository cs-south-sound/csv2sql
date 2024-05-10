# This script provides a function that takes a path to a directory
# and loops through the file to collect data from all CSVs and 
# returns them in as a single pandas DataFrame

import pandas as pd
import os

def extract_csvs(directory_path):
    """
    This is the main function that takes a directory path and returns
    a single DataFrame containing data from all CSVs in directory.

    Args:
        directory_path (str): Path to directory containing CSV files.

    Returns:
        pandas.Dataframe: A DataFrame with combined data from all CSVs.
    """

    # Create empty list to store DataFrames
    all_dataframes = []

    # Loop through directory to extract data from csvs
    for filename in os.listdir(directory_path):
        
        # Check if it's a csv file
        if filename.endswith('.csv'):
        
            # Construct full path for csv
            file_path = os.path.join(directory_path, filename)
            
            # Read csv as dataframe
            df = pd.read_csv(file_path)

            # Check if last row has some NaNs then drop
            # Drop last row
            df = df[:-1]

            # Append dataframe to list
            all_dataframes.append(df)

    # Concatenate all DataFrames into one
    combined_df = pd.concat(all_dataframes, ignore_index=True)

    return combined_df

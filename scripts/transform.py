# A script that provides a function which takes in a dataframe of Ark
# investment data and transforms the data to return a clean dataframe.

# Import packages
import pandas as pd

def transform_ark(dataframe):
    """
    This is the main function that takes a DataFrame of Ark Invest data 
    and returns a single DataFrame containing cleaned data.

    Args:
        dataframe (pandas.DataFrame): Original DataFrame of Ark data.

    Returns:
        pandas.Dataframe: A DataFrame with cleaned data from the original.
    """
    
    df = dataframe

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

    return df

from pathlib import Path

import pandas as pd


def load_and_clean_setup_data(filepath: Path, setup_name: str):
    """Load and standardize data from one setup"""
    df = pd.read_csv(filepath)
    print("Original data frame:")
    print(df)
    if df.isnull().values.any():
        df = df.dropna()
        print(f"Dropped rows with missing values in {setup_name} data.")
    if df.columns[1] == "temp_fahrenheit":
        df["temp_fahrenheit"] = (df["temp_fahrenheit"] - 32) *5/9
    # Standardize column names
    column_names = ["time_min", "temperature_C", "concentration_M", "pH", "yield_percent"]
    df.columns = column_names
    df['setup'] = setup_name
    print(df)
    return df

def combine_datasets(setup_a_data: pd.DataFrame, setup_b_data: pd.DataFrame):
    """Combine datasets from both setups"""
    combined_df = pd.concat([setup_a_data, setup_b_data], ignore_index=True)
    print(combined_df)
    return combined_df


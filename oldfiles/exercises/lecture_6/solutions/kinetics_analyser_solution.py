from typing import Any
import numpy as np
import pandas as pd


def calculate_reaction_rates(df: pd.DataFrame):
    """Calculate reaction rates for each time interval"""
    df["dt"] = df.groupby("setup")["time_min"].diff()
    df["dc"] = df.groupby("setup")["concentration_M"].diff()
    df["dT"] = df.groupby("setup")["temperature_C"].diff()
    df["dY"] = df.groupby("setup")["yield_percent"].diff()
    df["reaction_rates"] = df["dc"] / df["dt"]
    df["yield_change"] = df["dY"] / df["dt"]
    print(df)
    return df

    
def find_optimal_conditions(df: pd.DataFrame):
    """Analyze data to find optimal reaction conditions"""
    highest_rate = df["reaction_rates"].min() # Note: min() only returns the value!
    best_row_rates = df.loc[df["reaction_rates"].idxmin()] # Returns a df with the row of fastest rate. Note: idxmin() returns the index for the row containing the min. value! 
    average_rate = df.groupby("setup")["reaction_rates"].mean() #returns a Series
    average_yieldchange = df.groupby("setup")["yield_change"].mean() # returns a Series
    best_temperature_conditions = df.loc[df["yield_change"].idxmax()] # returns a df with row of highest yield change
    return highest_rate, best_row_rates, average_rate, average_yieldchange, best_temperature_conditions

def compare_setups(df: pd.DataFrame):
    """Compare performance between setups A and B"""
    results = find_optimal_conditions(df)
    highest_rate = results[0]
    best_row_rates = results[1]
    average_rate = results[2]
    average_yieldchange = results[3]

    # best temperature range
    best_T_range = results[4]
    upper_T = best_T_range.loc["temperature_C"]
    lower_T = best_T_range.loc["temperature_C"] - best_T_range.loc["dT"]

    print("-------------------------------------------------------------")
    print(f"The highest reaction rate ({highest_rate}) was detected in setup {best_row_rates.loc["setup"]}.")
    print(f"The highest average reaction rate ({average_rate.min()}) was detected in setup {average_rate.idxmin()}.")
    print(f"The highest average yield increase ({average_yieldchange.max()}) was detected in setup {average_yieldchange.idxmax()}.")
    print(f"The best temperature range was found in setup {best_T_range.loc["setup"]}: between {lower_T} and {upper_T} °C.")
    
    return

"""
wine_eda.py
-----------
Homework: Exploratory Data Analysis on the Wine dataset.

Goals:
1. Load and inspect the data
2. Perform exploratory analysis and visualizations
3. Apply PCA
"""

# Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA



# Main analysis function
def main():
    # --- 1. Load data ---
    print("Loading dataset...")
    wine = load_wine()
    df = pd.DataFrame(wine.data, columns=wine.feature_names)
    # add a 'target' column


    # print basic info (shape, first rows, summary statistics)

    # --- 2. Basic exploration ---
    # print class distribution and check for missing values

    # --- 3. Correlation analysis ---
    # compute correlation matrix (corr = df.corr(numeric_only=True))
    # plot and save a heatmap (e.g. 'heatmap.png')

    # --- 4. Visualisations ---
    # create and save a pairplot using a few selected features
    # create and save a boxplot comparing one feature across classes

    # --- 5. Scaling and PCA ---
    # separate features (X) and target (y)
    # scale the features using StandardScaler
    # apply PCA (2 components)
    # create a DataFrame with PCA results and target
    # plot and save a scatterplot of the first two components (color by target)

# Entry point
if __name__ == "__main__":
    main()
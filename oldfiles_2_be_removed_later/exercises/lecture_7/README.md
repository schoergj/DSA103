# Lecture 7: Exploratory Data Analysis
You have seen EDA in practice. Now, your task is to write a script doing the EDA so that you could reuse this for later explorations. We will follow up on the with some simple classification models (lecture 8).


## Goals

- Apply your data analysis skills from the Iris dataset to a new dataset — the Wine dataset from scikit-learn.
- Write a Python script (wine_eda.py) that performs a complete exploratory data analysis (EDA). You can use the template provided in the scripts folder (https://github.com/schoergj/DSA103/tree/main/python-chemistry-intro/scripts) or in your cloned fork ;)
- Make sure that the scripts has an organised structure and features clear comments. It should provide console output for the summary stats and save pictures of the plots.
- Make sure to push your work to your Repository

## Dataset

Use the built-in Wine dataset from sklearn.datasets by importing:
```python

from sklearn.datasets import load_wine

```

This dataset contains:

- 178 samples
- 13 numeric features describing chemical properties of wines
- 3 target classes (wine cultivars)

## Tasks
### 1. Load and inspect

- Load the dataset and convert it into a pandas DataFrame.
- Add a column named "target" for the wine class.
- Print the shape, column names, and first 5 rows.
- Show basic summary statistics (df.describe()).

## 2. Basic exploration

- Count how many samples belong to each class (value_counts()).
- Check for missing values (df.isna().sum()).
- Compute the correlation matrix and display it as a heatmap (seaborn.heatmap).

## 3. Visualisation

- Create and save the following plots (as PNG files):
- A pairplot of selected features (choose 4–5 interesting ones).
- A boxplot or violin plot comparing one feature across wine classes.
- A correlation heatmap (as above).

💡 Tip: label plots clearly and use plt.savefig() instead of plt.show() to produce output files.

## 4. Scaling and PCA

- Standardize the numeric features (StandardScaler).
- Perform PCA to reduce dimensions to 2 components.
- Plot a 2D scatterplot of the two principal components, colored by target class.

## Interpretation 

Interpret the EDA. Which patterns did you find, which anomalies, which correlations?


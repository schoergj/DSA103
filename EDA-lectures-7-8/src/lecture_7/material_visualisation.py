import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame({
    'A': [0.3, 0.4, 0.5, 0.7, 0.8, 1.1, 1.2, 1.3, 1.5, 1.9 ],
    'B': [1.1, 1.2, 1.3, 1.5, 1.7, 3.6, 2.1, 2.1, 2.3, 2.8],
    'C': [-0.1, 1.6, 1.5, 2.6, -1.2, 2.4, 2.8, 2.1, 1.3, 1.4]
    })
    
print(df.head())

# boxplot
plt.figure(figsize=(8, 5)) # width, height in inches for the "canvas"
sns.boxplot(data=df)
plt.title('Boxplot of Features A, B, and C')
plt.show()

# seaborn histogram
plt.figure(figsize=(10, 6)) # width, height in inches for the "canvas"
sns.histplot(data=df["A"], bins=5, kde=True) # kde = kernel density estimate
plt.title('Histogram of Feature A')
plt.show()

# matplotlib histogram
df.hist(bins=5) # bins = number of bars
plt.suptitle('Histograms of All Features', fontsize=16)
plt.show()

# pair plot
sns.pairplot(data=df, diag_kind='kde') # diag_kind = type of plot on diagonal')
plt.suptitle('Pairplot of Features A, B, and C', y=1.02)
plt.show()

# scatter plot
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='A', y='B', hue='C', palette='viridis')
plt.title('Scatter Plot of A vs B colored by C')
plt.show()

# correlation heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
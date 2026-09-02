"""
wine_eda_solution.py
--------------------

Solution for Wine dataset EDA + simple classification models

Goals:
1. Load and inspect the data
2. Perform exploratory analysis and visualizations
3. Apply PCA
4. Classification and evaluation
"""

# Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score


# Main analysis function
def main():
    # --- 1. Load data ---
    print("Loading dataset...")
    wine = load_wine()
    df = pd.DataFrame(wine.data, columns=wine.feature_names)
    df["target"] = wine.target

    print("\nData loaded successfully.")
    print(f"Shape: {df.shape}")
    print("\nFirst five rows:")
    print(df.head(), "\n")

    # 2. Basic exploration
    print("Info on dataset:")
    print(df.info(), "\n")
    
    print("Summary statistics:")
    print(df.describe(), "\n")

    print("Class distribution:")
    print(df["target"].value_counts(), "\n")

    print("Missing values:")
    print(df.isna().sum(), "\n")


    # set display options so that the print-statement is not truncated
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    # Mean of features per target
    print("\nMean feature values per target:")
    print(df.groupby('target').mean())

    # Std.dev. of features per target
    print("\nStdandard deviation for feature values per target:")
    print(df.groupby('target').std())

    # variance of features per target
    print("\nVariance of feature values per target:")
    print(df.groupby('target').var())

    # 3. Correlation analysis
    corr = df.corr(numeric_only=True)
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, cmap="coolwarm", center=0)
    plt.title("Correlation Heatmap - Wine Dataset")
    plt.tight_layout()
    plt.savefig("heatmap.png")
    plt.close()
    print("Saved heatmap.png")

    # 4. Visualizations
    selected_features = ["alcohol", "flavanoids", "malic_acid", "color_intensity", "proline"]
    sns.pairplot(df, vars=selected_features, hue="target", palette="Set1")
    plt.savefig("pairplot.png")
    plt.close()
    print("Saved pairplot.png")

    plt.figure(figsize=(8, 5))
    sns.boxplot(x="target", y="flavanoids", data=df)
    plt.title("Flavonoid Content by Wine Class")
    plt.tight_layout()
    plt.savefig("boxplot.png")
    plt.close()
    print("boxplot.png")

    # 5. Scaling and PCA
    X = df.drop("target", axis=1)
    y = df["target"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)

    pca_df = pd.DataFrame(X_pca, columns=["PC1", "PC2"])
    pca_df["target"] = y

    plt.figure(figsize=(8, 6))
    sns.scatterplot(x="PC1", y="PC2", hue="target", data=pca_df, palette="Set1")
    plt.title("PCA (2 Components) - Wine Dataset")
    plt.tight_layout()
    plt.savefig("pca_scatter.png")
    plt.close()
    print("Saved pca_scatter.png")

    print("\nExplained variance ratio (PCA):")
    print(pca.explained_variance_ratio_)
    print(f"Cumulative variance explained: {pca.explained_variance_ratio_.sum():.3f}\n")

    # 6. Classification on original data
    print("--------------------------------------------")
    print("Classification models on original data.\n")
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    # Logistic regression
    logreg = LogisticRegression(max_iter=1000)
    logreg.fit(X_train, y_train)
    y_pred = logreg.predict(X_test)

    # acc = accuracy_score(y_test, y_pred)
    # print(f"Logistic Regression - model accuracy: {acc:.3f}\n")
    print("Logistic Regression - train accuracy:", logreg.score(X_train, y_train))
    print("Logistic Regression - test accuracy:", logreg.score(X_test, y_test))

    print("Logistic Regression - confusion matrix:")
    print(confusion_matrix(y_test, y_pred), "\n")

    # print("Logistic regression - classification report:") # just another report to get some stats on the model
    # print(classification_report(y_test, y_pred))


    # Decision tree
    tree = DecisionTreeClassifier(max_depth=3, random_state=42)
    tree.fit(X_train, y_train)
    y_pred = tree.predict(X_test)


    print("Decision Tree - train accuracy:", tree.score(X_train, y_train))
    print("Decision Tree - test accuracy:", tree.score(X_test, y_test))
    print("Decision Tree - confusion matrix:")
    print(confusion_matrix(y_test, y_pred), "\n")

    # Random forest
    rf = RandomForestClassifier(
    n_estimators=100,      # number of trees in the forest
    max_depth=None,        # let the trees expand fully
    random_state=42,       # for reproducibility
    )
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)

    print("Random Forest Classifier - training accuracy:", rf.score(X_train, y_train))
    print("Random Forest Classifier - test accuracy:", rf.score(X_test, y_test))
    print("Random Forest Classifier - confusion matrix:")
    print(confusion_matrix(y_test, y_pred), "\n")


    # 7. Classification on reduced dataset from PCA
    print("--------------------------------------------")
    print("Classification models on principal components.\n")
    X_train, X_test, y_train, y_test = train_test_split(
        X_pca, y, test_size=0.2, random_state=42
    )

    # Logistic regression
    logreg = LogisticRegression(max_iter=1000)
    logreg.fit(X_train, y_train)
    y_pred = logreg.predict(X_test)

    # acc = accuracy_score(y_test, y_pred)
    # print(f"Logistic Regression - model accuracy: {acc:.3f}\n")
    print("Logistic Regression - PC train accuracy:", logreg.score(X_train, y_train))
    print("Logistic Regression - PC test accuracy:", logreg.score(X_test, y_test))

    print("Logistic Regression - PC confusion matrix:")
    print(confusion_matrix(y_test, y_pred), "\n")

    # print("Logistic regression - classification report:") # just another report to get some stats on the model
    # print(classification_report(y_test, y_pred))


    # Decision tree
    tree = DecisionTreeClassifier(max_depth=3, random_state=42)
    tree.fit(X_train, y_train)
    y_pred = tree.predict(X_test)


    print("Decision Tree - PC train accuracy:", tree.score(X_train, y_train))
    print("Decision Tree - PC test accuracy:", tree.score(X_test, y_test))
    print("Decision Tree - PC confusion matrix:")
    print(confusion_matrix(y_test, y_pred), "\n")

    # Random forest
    rf = RandomForestClassifier(
    n_estimators=100,      # number of trees in the forest
    max_depth=None,        # let the trees expand fully
    random_state=42,       # for reproducibility
    )
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)

    print("Random Forest Classifier - PC training accuracy:", rf.score(X_train, y_train))
    print("Random Forest Classifier - PC test accuracy:", rf.score(X_test, y_test))
    print("Random Forest Classifier - PC confusion matrix:")
    print(confusion_matrix(y_test, y_pred), "\n")

    print("\nAnalysis complete. Figures saved to current working directory.")

# Entry point
if __name__ == "__main__":
    main()

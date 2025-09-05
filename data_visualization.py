"""
Ubuntu Data Explorer
--------------------
This script demonstrates:
1. Loading and exploring a dataset (CSV or Iris dataset)
2. Performing basic data analysis
3. Visualizing patterns with matplotlib and seaborn
4. Extracting insights from the analysis

Dataset: User-provided CSV or Iris dataset (default)
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import os

def load_dataset():
    """Load dataset from CSV or fallback to Iris dataset."""
    print("Would you like to load your own CSV dataset?")
    choice = input("Enter CSV file path or press Enter to use the Iris dataset: ").strip()

    if choice:
        try:
            if not os.path.exists(choice):
                print(f"✗ File not found: {choice}. Falling back to Iris dataset.")
                return load_iris_dataset()

            df = pd.read_csv(choice)
            print(f"✓ Dataset successfully loaded from {choice}")
            return df
        except Exception as e:
            print(f"✗ Error loading CSV: {e}. Falling back to Iris dataset.")
            return load_iris_dataset()
    else:
        return load_iris_dataset()

def load_iris_dataset():
    """Load the Iris dataset into a pandas DataFrame."""
    iris = load_iris(as_frame=True)
    df = iris.frame
    df["species"] = iris.target_names[df["target"]]  # add species names
    df.drop(columns="target", inplace=True)          # drop numeric target col
    print("✓ Iris dataset successfully loaded.")
    return df

def explore_data(df):
    """Explore structure, data types, and missing values."""
    print("\n--- Data Overview ---")
    print(df.head())

    print("\n--- Data Types ---")
    print(df.dtypes)

    print("\n--- Missing Values ---")
    print(df.isnull().sum())

    # Handle missing values (drop them for simplicity)
    df = df.dropna()
    return df

def basic_analysis(df):
    """Perform basic statistics and grouping analysis."""
    print("\n--- Summary Statistics ---")
    print(df.describe())

    # Only run grouping if a categorical column exists
    cat_cols = df.select_dtypes(include=["object", "category"]).columns
    num_cols = df.select_dtypes(include=["number"]).columns

    if len(cat_cols) > 0 and len(num_cols) > 0:
        group_col = cat_cols[0]
        print(f"\n--- Mean of numerical features grouped by {group_col} ---")
        grouped = df.groupby(group_col).mean(numeric_only=True)
        print(grouped)

        print("\nObservation:")
        print(f"→ Grouping by {group_col} shows distinct differences in numerical features.")
    else:
        print("\n(No categorical column found for grouping analysis.)")

def visualize_data(df):
    """Generate multiple visualizations if enough numerical columns exist."""
    num_cols = df.select_dtypes(include=["number"]).columns

    if len(num_cols) < 2:
        print("\n✗ Not enough numerical columns to generate all plots.")
        return

    # 1. Line chart (first numeric column across samples)
    plt.figure(figsize=(8, 4))
    plt.plot(df.index, df[num_cols[0]], label=num_cols[0], color="green")
    plt.title(f"{num_cols[0]} Trend Across Samples")
    plt.xlabel("Sample Index")
    plt.ylabel(num_cols[0])
    plt.legend()
    plt.tight_layout()
    plt.show()

    # 2. Bar chart (mean of first numeric column per category if available)
    cat_cols = df.select_dtypes(include=["object", "category"]).columns
    if len(cat_cols) > 0:
        plt.figure(figsize=(6, 4))
        sns.barplot(x=cat_cols[0], y=num_cols[0], data=df, estimator="mean", palette="viridis")
        plt.title(f"Average {num_cols[0]} by {cat_cols[0]}")
        plt.xlabel(cat_cols[0])
        plt.ylabel(f"Avg {num_cols[0]}")
        plt.tight_layout()
        plt.show()

    # 3. Histogram (distribution of second numeric column)
    plt.figure(figsize=(6, 4))
    plt.hist(df[num_cols[1]], bins=15, color="skyblue", edgecolor="black")
    plt.title(f"Distribution of {num_cols[1]}")
    plt.xlabel(num_cols[1])
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

    # 4. Scatter plot (first two numeric columns)
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x=num_cols[0], y=num_cols[1], hue=cat_cols[0] if len(cat_cols) > 0 else None, data=df, palette="deep")
    plt.title(f"{num_cols[0]} vs {num_cols[1]}")
    plt.xlabel(num_cols[0])
    plt.ylabel(num_cols[1])
    plt.legend(title=cat_cols[0] if len(cat_cols) > 0 else "Legend")
    plt.tight_layout()
    plt.show()

def main():
    print("Welcome to Ubuntu Data Explorer\n")

    df = load_dataset()
    if df is None or df.empty:
        print("✗ No dataset available. Exiting.")
        return

    df = explore_data(df)
    basic_analysis(df)
    visualize_data(df)

    print("\nAnalysis complete. Community enriched.")

if __name__ == "__main__":
    main()

# Data_Visualization
# Ubuntu Data Explorer

A Python project that demonstrates **data loading, exploration, analysis, and visualization** while embracing Ubuntu principles of **Community, Respect, Sharing, and Practicality**.

This script allows you to either **load your own CSV dataset** or **use the classic Iris dataset** if no file is provided. It walks through the complete data analysis workflow — from loading and cleaning the data to generating insights with visualizations.

---

## Features
- Load and explore datasets from a **CSV file** or fallback to **Iris dataset**.
- Display the structure, data types, and missing values.
- Clean the dataset (drop missing values for simplicity).
- Compute summary statistics (`mean`, `median`, `std`) with `.describe()`.
- Perform group-by analysis on categorical features (average values per category).
- Generate **4 visualizations**:
  - Line chart (trend of first numerical column across samples)
  - Bar chart (average of first numerical column by category)
  - Histogram (distribution of second numerical column)
  - Scatter plot (first numeric column vs second numeric column, optionally colored by category)

---

## Requirements
- Python 3.7+
- Required libraries:
  - pandas
  - matplotlib
  - seaborn
  - scikit-learn
 
    
pip install pandas matplotlib seaborn scikit-learn
You will be prompted:

Would you like to load your own CSV dataset?
Enter CSV file path or press Enter to use the Iris dataset:


Option 1: Enter a valid CSV file path (e.g., data/sales.csv)

Option 2: Press Enter to use the Iris dataset

The script will:

Preview the dataset (.head())

Show summary statistics and grouped means (if categorical columns exist)

Display four visualizations

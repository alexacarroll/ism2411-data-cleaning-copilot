import pandas as pd

# Load the raw sales data into a pandas dataframe
def load_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    return df

# Standardize colum names to lowercase and replace spaces with underscores.
# Prevents errors later when referencing colums by name>
def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()            # removes leading and trailing spaces
        .str.lower()            # lowercase
        .str.replace(" ", "_")  # underscores instead of spaces
    )
    return df

# Remove unwanted spaces from string columns such as product_name and category.
# This ensures that identical-looking items actually match when grouped or analyzed.
def strip_text_whitespace(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    text_columns = ["product_name", "category"]
    for col in text_columns:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()
    return df

# Handle missing values in price and quantity.
# In this dataset, rows missing these values are incomplete, so we drop them.
def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.dropna(subset=["price", "qty"])
    return df

# Remove rows with negative prices or quantities because these indicate data entry errors.
def remove_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["qty"] = pd.to_numeric(df["qty"], errors="coerce")
    df = df.dropna(subset=["price", "qty"])
    df = df[(df["price"] >= 0) & (df["qty"] >= 0)]
    return df

if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = strip_text_whitespace(df_clean)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)

    df_clean.to_csv(cleaned_path, index=False)
    print("Cleaning complete. First few rows:")
    print(df_clean.head())




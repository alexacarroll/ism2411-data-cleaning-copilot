This project demonstrates a complete "data cleaning pipeline" in Python using 'pandas'.

Project Overview
-------------------------------------------------------------------------------------
The goal of this project is to take a messy CSV file (`sales_data_raw.csv') and clean it using Python.
All cleaning operations are performed programmatically - the raw file itself is never modified manually.

Key objectives:
- Practice reading, cleaning, and exporting data with pandas.
- Use GitHub Copilot to generate helper functions, then refine them.
- Build a small but complete, GitHub-ready Python project.

The script 'src?data_cleaning.py` performs the following steps:

1. Load Data
   - Reads 'sales_data_raw.csv' from 'data/raw`.

2. Standardize Column Names
   - Converts all column names to lowercase and replaces spaces with underscores (e.g., '"Price"' -> '"price"`).

3. Trim Text Columns
   - Removes extra whitespace in text columns like 'product_name' and 'category`.

4. Handle Missing Values
   - Drops rows missing essential fields ('price' or `qty').

5. Remove Invalid Rows
   - Converts columns to numeric types and removes rows with negative or invalid values.

6. Export Clean Data
   - Writes the cleaned DataFrame to 'data/processed/sales_data_clean.csv`.


How to Run the Script
1. Prerequisites
Make sure you have Python 3 and `pandas' installed:

```bash
pip install pandas

2. Run the Script
From the project root folder, run:
 - python src/data_cleaning.py
If successful, you’ll see:
 - Cleaning complete. First few rows:
and the cleaned file will appear here:
 - data/processed/sales_data_clean.csv

Product Structure
ism2411-data-cleaning-copilot/
├── data/
│   ├── raw/
│   │   └── sales_data_raw.csv
│   └── processed/
│       └── sales_data_clean.csv
├── src/
│   └── data_cleaning.py
├── README.md
└── reflection.md

Example Output
Cleaning complete. First few rows:
   order_id  product_name  category  price  qty
0     10001  Widget A      Tools     9.99   3
1     10002  Widget B      Tools    14.50   1
2     10003  Gadget C      Tech     29.99   2


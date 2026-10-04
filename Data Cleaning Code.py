# 1. Remove duplicate entries
df_clean = df.drop_duplicates()

# 2. Fix Data Types
df_clean['InvoiceDate'] = pd.to_datetime(df_clean['InvoiceDate'])
df_clean['Description'] = df_clean['Description'].astype(str)

# 3. Handle Missing Values
df_clean['CustomerID'] = df_clean['CustomerID'].fillna('Guest')
df_clean['Description'] = df_clean['Description'].replace('nan', 'Unknown Product')

# 4. Filter out negative and zero quantities/prices
df_clean = df_clean[(df_clean['Quantity'] > 0) & (df_clean['UnitPrice'] > 0)]

# 5. Feature Engineering: Total Spend per line item
df_clean['TotalAmount'] = df_clean['Quantity'] * df_clean['UnitPrice']

print(f"Cleaned Dataset Shape: {df_clean.shape}")
print(f"Total Rows Removed: {len(df) - len(df_clean)}")
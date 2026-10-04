plt.figure(figsize=(8, 6))
numeric_cols = ['Quantity', 'UnitPrice', 'TotalAmount']
corr_matrix = df_clean[numeric_cols].corr()

sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, fmt=".2f")
plt.title('Correlation Matrix of Numeric Features')
plt.show()
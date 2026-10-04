import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Set visual styles
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Load dataset
df = pd.read_csv("ecommerce_sales_data.csv")

# Display shape and initial information
print(f"Dataset Shape: {df.shape}")
print(df.info())
print(df.head())
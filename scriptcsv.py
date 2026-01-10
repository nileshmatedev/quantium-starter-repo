import pandas as pd
import os

data_folder = os.path.join(os.path.dirname(__file__),'data')

data_folder_files = []
for i in range(3):
    file_path = os.path.join(data_folder,f'daily_sales_data_{i}.csv')
    df = pd.read_csv(file_path)
    data_folder_files.append(df)

df_combined = pd.concat(data_folder_files, ignore_index=True)
print(f"loaded: {len(df_combined)} total rows")

df_filtered = df_combined[df_combined['product'].str.lower()== 'pink morsel']
print(f"After Filter: {len(df_filtered)} pink morsel rows")

df_filtered = df_filtered.copy()
df_filtered['price'] = df_filtered['price'].str.replace('$','').astype(float)

df_filtered['sales'] = df_filtered['quantity'] * df_filtered['price']
print(f"sales calculated")

output_df = df_filtered[['sales','date', 'region']].copy()

output_df.columns = ['Sales', 'Date', 'Region']
print(f"Column renamed: {list(output_df.columns)}")

output_path = os.path.join(os.path.dirname(__file__), 'pink_morsels_sales.csv')
output_df.to_csv(output_path, index=False)
print(f"✓ Saved to: pink_morsels_sales.csv")
print(f"✓ Total rows: {len(output_df)}")
print(output_df.head())
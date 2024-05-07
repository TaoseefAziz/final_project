import pandas as pd

# Define the input and output filenames
input_file = "device_urls.csv"
output_file = "device_urls_filtered.csv"

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(input_file)

# Create an empty list to store filtered rows
filtered_rows = []

# Loop through each row in the DataFrame
for index, row in df.iterrows():
  manufacturer = row["manufacturer"]
  device = row["device"]
  # Check if manufacturer + "_" is present in device
  if manufacturer + "_" in device:
    filtered_rows.append(row)

# Create a new DataFrame from the filtered rows
filtered_df = pd.DataFrame(filtered_rows)

# Write the filtered DataFrame to a new CSV file
filtered_df.to_csv(output_file, index=False)

# Print confirmation message
print(f"Data filtered and saved to: {output_file}")

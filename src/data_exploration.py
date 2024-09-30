import pandas as pd

# Load the dataset
file_path = 'data/Housing.csv'  # Update the path to where your file is located
housing_data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(housing_data.head())

# Display the structure of the dataset
print("\nDataset Info:")
print(housing_data.info())

# Display summary statistics
print("\nSummary Statistics:")
print(housing_data.describe())

import pandas as pd

# Load the dataset
file_path = 'data/Housing.csv'  # Update the path to where your file is located
housing_data = pd.read_csv(file_path)

# Display the initial shape of the dataset
print("Initial shape of the dataset:", housing_data.shape)

# Handling missing values
# You can choose to drop or fill missing values; here, we will drop rows with any missing values
housing_data.dropna(inplace=True)

# Display the shape after dropping missing values
print("Shape after dropping missing values:", housing_data.shape)

# Encoding categorical variables
# If there are any categorical features, you can use one-hot encoding or label encoding
housing_data = pd.get_dummies(housing_data, drop_first=True)

# Normalize the data (optional)
# If your features vary greatly in scale, normalization may be necessary
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
housing_data[['area', 'bedrooms', 'price']] = scaler.fit_transform(housing_data[['area', 'bedrooms', 'price']])

# Display the first few rows of the preprocessed data
print("\nFirst few rows after preprocessing:")
print(housing_data.head())

# Save the preprocessed data to a new CSV file
housing_data.to_csv('data/Preprocessed_Housing.csv', index=False)
print("Preprocessed data saved to 'data/Preprocessed_Housing.csv'.")
    
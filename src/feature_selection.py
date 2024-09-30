import pandas as pd

# Load the preprocessed dataset
file_path = 'data/Preprocessed_Housing.csv'
housing_data = pd.read_csv(file_path)

# Display the initial shape of the dataset
print("Initial shape of the preprocessed dataset:", housing_data.shape)

# Display correlation matrix to analyze feature importance
correlation_matrix = housing_data.corr()
print("\nCorrelation matrix:")
print(correlation_matrix)

# Visualizing the correlation matrix (optional)
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Feature selection: removing less useful features
# For example, let's remove 'furnishingstatus_semi-furnished' and 'furnishingstatus_unfurnished'
housing_data.drop(['furnishingstatus_semi-furnished', 'furnishingstatus_unfurnished'], axis=1, inplace=True)

# Display the shape after removing features
print("Shape after removing less useful features:", housing_data.shape)

# Save the updated dataset
housing_data.to_csv('data/Feature_Selected_Housing.csv', index=False)
print("Updated dataset saved to 'data/Feature_Selected_Housing.csv'.")

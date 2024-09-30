import pandas as pd

def load_data(file_path):
    """
    Load the dataset from the specified CSV file path.
    
    Parameters:
        file_path (str): Path to the CSV file.
    
    Returns:
        DataFrame: Loaded data as a pandas DataFrame.
    """
    try:
        # Load the data
        data = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")

if __name__ == "__main__":
    # Specify the path to your dataset
    file_path = 'data/Housing.csv'  # Change this if your file path is different
    housing_data = load_data(file_path)

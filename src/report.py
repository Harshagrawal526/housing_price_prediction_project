import pandas as pd
import matplotlib.pyplot as plt

# Load the feature-selected dataset
file_path = 'data/Feature_Selected_Housing.csv'
housing_data = pd.read_csv(file_path)

# Load the evaluation results (you can customize this section)
results = {
    'Model': ['Linear Regression', 'Polynomial Regression (Degree 1)', 'Polynomial Regression (Degree 2)', 'Polynomial Regression (Degree 3)'],
    'MSE': [0.35,0.35, 13061398044323421880320.00, 2.43],
    'R² Score': [0.63,0.63, -9023919449496214306816.00, -1.66]
}

results_df = pd.DataFrame(results)

# Save the results to a CSV file
results_df.to_csv('data/Model_Evaluation_Results.csv', index=False)
print("Model evaluation results saved to 'data/Model_Evaluation_Results.csv'.")

# Plotting the MSE and R² scores
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.bar(results_df['Model'], results_df['MSE'], color='blue')
plt.title('Mean Squared Error')
plt.xticks(rotation=45)
plt.ylabel('MSE')

plt.subplot(1, 2, 2)
plt.bar(results_df['Model'], results_df['R² Score'], color='orange')
plt.title('R² Scores')
plt.xticks(rotation=45)
plt.ylabel('R² Score')

plt.tight_layout()
plt.savefig('data/model_evaluation_plot.png')
plt.show()

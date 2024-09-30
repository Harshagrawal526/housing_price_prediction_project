# Housing Price Prediction Project

## Project Overview
This project aims to predict housing prices using a dataset that includes various features related to housing conditions. The project utilizes polynomial regression for model fitting and evaluation, as well as feature selection and extraction techniques.

## Dataset
The dataset used for this project is the Housing dataset obtained from Kaggle. You can find it [here](https://www.kaggle.com/datasets/ashydv/housing-dataset).

## Project Structure
```
housing_price_prediction_project/
│
├── data/
│   ├── Feature_Selected_Housing.csv    # Dataset after feature selection
│   ├── Housing.csv                      # Raw dataset
│   ├── Model_Evaluation_Results.csv     # Results of model evaluation
│   └── Preprocessed_Housing.csv         # Preprocessed dataset
│
├── README.md                            # Documentation for the project
│
├── reports/                             # Directory for report files
│   ├── figures/                         # Directory to store visualizations
│   │   ├── correlation_heatmap.png      # Correlation heatmap plot
│   │   ├── correlation_matrix.png        # Correlation matrix plot
│   │   ├── housing_price_distribution.png # Distribution plot of housing prices
│   │   ├── model_evaluation_plot.png    # Model evaluation plot
│   │   └── residual_plot.png             # Residual plot
│   └── results.md                       # Results and findings of the project
│
├── requirements.txt                     # Required packages for the project
│
└── src/                                 # Source code for the project
    ├── __init__.py                      # Initialization for the package
    ├── data_loading.py                  # Data loading functionality
    ├── data_exploration.py               # Data exploration and initial analysis
    ├── feature_selection.py              # Feature selection techniques
    ├── preprocessing.py                  # Data preprocessing techniques
    ├── model.py                          # Model training and evaluation logic
    └── report.py                        # Generates reports based on analysis
```
## Installation
To set up the project environment, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd housing_price_prediction_project
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```


## Usage
1. Load the data using `data_loading.py`.
2. Explore the data with `data_exploration.py`.
3. Perform feature selection with `feature_selection.py`.
4. Preprocess the data with `preprocessing.py`.
5. Evaluate models and visualize results using `model.py` and `visualizations.py`.

## Results
The results of the project can be found in the `reports/results.md` file. Key findings include:
- Selected features for model training.
- Performance metrics of polynomial regression models.
- Visualizations of the correlation matrix, model evaluation, and residual plots.

## Conclusion
This project demonstrates the application of machine learning techniques in predicting housing prices. The methodologies applied include data exploration, feature selection, polynomial regression, and visualization of results.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

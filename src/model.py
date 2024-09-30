# import pandas as pd
# from sklearn.model_selection import KFold, train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, r2_score

# # Load the feature-selected dataset
# file_path = 'data/Feature_Selected_Housing.csv'
# housing_data = pd.read_csv(file_path)

# # Separate features and target variable
# X = housing_data.drop('price', axis=1)  # Features
# y = housing_data['price']  # Target variable

# # K-Fold Cross-Validation
# kf = KFold(n_splits=5, shuffle=True, random_state=42)  # Using 5 folds
# mse_scores = []
# r2_scores = []

# for train_index, test_index in kf.split(X):
#     X_train, X_test = X.iloc[train_index], X.iloc[test_index]
#     y_train, y_test = y.iloc[train_index], y.iloc[test_index]

#     # Create and fit the model
#     model = LinearRegression()
#     model.fit(X_train, y_train)

#     # Predict on the test set
#     y_pred = model.predict(X_test)

#     # Calculate metrics
#     mse = mean_squared_error(y_test, y_pred)
#     r2 = r2_score(y_test, y_pred)
#     mse_scores.append(mse)
#     r2_scores.append(r2)

# # Display average scores
# print(f"Average Mean Squared Error: {sum(mse_scores) / len(mse_scores):.2f}")
# print(f"Average R² Score: {sum(r2_scores) / len(r2_scores):.2f}")





import pandas as pd
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

# Load the feature-selected dataset
file_path = 'data/Feature_Selected_Housing.csv'
housing_data = pd.read_csv(file_path)

# Separate features and target variable
X = housing_data.drop('price', axis=1)  # Features
y = housing_data['price']  # Target variable

# K-Fold Cross-Validation
kf = KFold(n_splits=5, shuffle=True, random_state=42)  # Using 5 folds
degree_scores = {}

# Test polynomial regression for degrees 1 to 3
for degree in range(1, 4):
    mse_scores = []
    r2_scores = []
    
    poly = PolynomialFeatures(degree=degree)
    X_poly = poly.fit_transform(X)  # Transform features to polynomial features

    for train_index, test_index in kf.split(X_poly):
        X_train, X_test = X_poly[train_index], X_poly[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]

        # Create and fit the model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Predict on the test set
        y_pred = model.predict(X_test)

        # Calculate metrics
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        mse_scores.append(mse)
        r2_scores.append(r2)

    # Store the average scores for this degree
    degree_scores[degree] = {
        'Average MSE': sum(mse_scores) / len(mse_scores),
        'Average R² Score': sum(r2_scores) / len(r2_scores)
    }

# Display average scores for each polynomial degree
for degree, scores in degree_scores.items():
    print(f"Degree {degree}:")
    print(f"  Average Mean Squared Error: {scores['Average MSE']:.2f}")
    print(f"  Average R² Score: {scores['Average R² Score']:.2f}\n")

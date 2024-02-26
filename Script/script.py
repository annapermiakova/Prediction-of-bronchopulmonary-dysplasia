import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas as pd
import os

def logistic_regression_calculator(X, coefficients, intercept):
    # Calculate logit(p)
    logit_p = intercept
    for i, coef in enumerate(coefficients):
        logit_p += coef * X[i]

    # Calculate probability
    probability = 1 / (1 + np.exp(-logit_p))
    return probability

def main():
    # Given coefficients and intercept
    coefficients = [-0.6808858463736446, 0.6762455396834283, -0.6226713869756503, 0.3704844403036638, 0.7862307732878744]
    intercept = 1.1853711415943018

    # Test values (in original format)
    X_test = [720, 5, 7, 4, 23]  # Example values in original format

    # Determine the path to the Excel file
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'BLD_178.xlsx')

    # Load your training data
    training_data = pd.read_excel(file_path)

    # Extract features from the training data (assuming 'BPD' contains the target variable and other columns are features)
    X_train = training_data.drop(columns=['BPD'])

    # Fit the scaler on the training data
    scaler = StandardScaler()
    scaler.fit(X_train)

    # Standardize the test data
    X_test_standardized = scaler.transform([X_test])

    # Calculate probability using the logistic regression equation
    probability = logistic_regression_calculator(X_test_standardized[0], coefficients, intercept)

    # Convert probability to percentage and format the output
    probability_percentage = probability * 100
    probability_percentage_formatted = "{:.20f}".format(probability_percentage)

    print("Probability:", probability_percentage_formatted, "%")

if __name__ == "__main__":
    main()

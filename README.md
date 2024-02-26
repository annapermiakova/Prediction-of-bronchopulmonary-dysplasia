![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=%white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)

# About the project
The project is devoted to the development of an early prediction model for clinically significant bronchopulmonary dysplasia in very premature infants.
 # Project result 
  probability calculator
# For whom 
pediatricians, neonatologists

# Project content

- File  [BLD_178.xlsx](BLD_178.xlsx) contains primary information about patients.
- File [BLD_178.ipynb](BLD_178.ipynb) contains descriptive and comparative analysis as well as machine learning models

# Brief description of the project

This study is aimed at development of the model for early prediction of clinically significant bronchopulmonary dysplasia in premature infants.

Machine learning algorithms were used to build the prognostic model: log-regression, support vector machine, random forest method, and gradient boosting. Five variables were used: birth weight, Apgar score at 5 minutes, Silverman score, number of days of invasive ventilatory support, median values fraction of oxygen in the inhaled air measured in the first seven days of life.

Among the four studied prediction algorithms, logistic regression model was chosen as the final model with metrics: AUC=0.840, accuracy 0.818, sensitivity 0.972, specificity 0.666.
The practical application of the modeling results was implemented in the form of an Excel-based calculator.

## Using a Probability Calculator

### 1.Install Dependencies: 
Make sure you have Python installed along with all the required libraries. You can install the dependencies using pip:

```sh
pip install -r requirements.txt
```

### 3.Run the Script: 
 Execute the script from the command line, providing the path to the Excel data file. For example:

 ```sh
 python script.py
```

 ### 4.Input Data:
When running the script, you may need to input additional data such as file paths or algorithm parameters. Follow the prompts to enter the required information.
 
# Files
[script.py](script.py) The main script that performs logistic regression on data from an Excel file.

[BLD_178.xlsx](BLD_178.xlsx) Sample data file used in the script.

## Dependencies
numpy: Library for numerical computations with arrays and matrices in Python.

pandas: Library for data manipulation and analysis in tabular form.

scikit-learn: Library containing machine learning algorithms and tools for data analysis.


## Authors

* **Anna Permiakova** [med-python](https://github.com/med-python)




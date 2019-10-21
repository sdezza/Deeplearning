# Data Preprocessing
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import Imputer

# Importing dataset
dataset = pd.read_csv('')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# missing data strategy
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

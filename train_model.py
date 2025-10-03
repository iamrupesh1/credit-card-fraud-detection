# train_model.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from imblearn.over_sampling import SMOTE
import joblib

# Load data
data = pd.read_csv(r"data/creditcard.csv")

# Split features and target
X = data.drop(['Class'], axis=1)
Y = data['Class']

# Split into training and test sets
xTrain, xTest, yTrain, yTest = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)

# Handle class imbalance using SMOTE
sm = SMOTE(random_state=42)
xTrain_res, yTrain_res = sm.fit_resample(xTrain, yTrain)

# Train Random Forest
rfc = RandomForestClassifier(n_estimators=100, random_state=42)
rfc.fit(xTrain_res, yTrain_res)

# Evaluate
yPred = rfc.predict(xTest)
print("Accuracy:", accuracy_score(yTest, yPred))
print("Precision:", precision_score(yTest, yPred))
print("Recall:", recall_score(yTest, yPred))
print("F1 Score:", f1_score(yTest, yPred))
print("Confusion Matrix:\n", confusion_matrix(yTest, yPred))

# Save the trained model
joblib.dump(rfc, "model.pkl")
print(" Model saved as model.pkl")

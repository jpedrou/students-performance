import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.pipeline import Pipeline

from feature_engine.encoding import OrdinalEncoder
from feature_engine.imputation import MeanMedianImputer, CategoricalImputer


# The objective is to predict the math score
# target = math score



# Loading data
df = pd.read_csv("data/StudentsPerformance.csv")
df['test preparation course'].unique()

# Split into train and test
df.shape

X_train, X_dev, y_train, y_dev = train_test_split(
    df.drop("math score", axis=1), df["math score"], test_size=0.05, random_state=42
)

# Checking Missing Values
X_train.isnull().mean()
X_dev.isnull().mean()

y_train.isnull().mean()
y_dev.isnull().mean()


# Checking train info
X_train.info()

num_vars = list(X_train.select_dtypes(np.number).columns)
cat_vars = list(X_train.select_dtypes(np.object_).columns)

# making model pipeline
model_pipe = Pipeline(
    [
        (
            "Numerical Imputation",
            MeanMedianImputer(variables=num_vars, imputation_method="mean"),
        ),
        (
            "Categorical Imputation",
            CategoricalImputer(variables=cat_vars, imputation_method="missing", fill_value='Missing'),
        ),
        (
            "Categorical Encoder",
            OrdinalEncoder(variables=cat_vars, encoding_method="ordered"),
        ),
        (
            "Random  Forest Regressor Model",
            RandomForestRegressor(
                n_estimators=100, random_state=42
            ),
        ),
    ]
)

model_pipe.fit(X_train, y_train)

y_train_pred = model_pipe.predict(X_train)

print('Train RMSE: ', np.sqrt(mean_squared_error(y_train, y_train_pred)))
print('Train R2: ', r2_score(y_train, y_train_pred))

y_dev_pred = model_pipe.predict(X_dev)

print('Dev RMSE: ', np.sqrt(mean_squared_error(y_dev, y_dev_pred)))
print('Dev R2: ', r2_score(y_dev, y_dev_pred))

joblib.dump(model_pipe,  'model_pipeline.pickle')



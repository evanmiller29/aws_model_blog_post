import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.externals import joblib
from sklearn.metrics import r2_score

import zipfile
# Defining global variables

rand_seed = 42

# Reading in the data

df = pd.read_csv('uk-housing-prices-paid/price_paid_records.csv', low_memory=True)
print(df.columns.tolist())

# Dropping all columns instead of price, property type, old/new, duration.
# Some of these columns have odd input values, but since this is just a test example I'm not too worried about that.

df = df[['Price', 'Property Type', 'Old/New', 'Duration']]

# Outputting the possible values for the inputs because we'll need to know.

print(df['Property Type'].value_counts())
print(df['Old/New'].value_counts())
print(df['Duration'].value_counts())

# Splitting the data into train/test before building the model

y = df['Price']
X = df.drop('Price', axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=rand_seed)

# Building a pipeline to handle build a simple model. I'm just building a simple model, it probably won't be that accurate but that's OK.

cat_featuress = ['Property Type', 'Old/New', 'Duration']
cat_feat_processer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))]
)

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', cat_feat_processer, cat_featuress)])

model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', ElasticNet(random_state=rand_seed))
    ]
)

model.fit(X_train, y_train)
preds = model.predict(X_test)

print(r2_score(y_test, preds))
# Ha thank god this isn't a Kaggle competition, this model is horrible.

joblib.dump(model, 'house_price_model.pkl')

# Zipping model file for the lambda layers
zipfile.ZipFile('model.zip', mode='w').write("house_price_model.pkl")

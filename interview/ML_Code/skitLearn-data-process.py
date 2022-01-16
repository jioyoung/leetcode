
import pandas as pd
all_df = [] # input data set

# category variables
cat_feature_set = ['cat1', 'cat2']
all_df.loc[:, cat_feature_set] = all_df.loc[:, cat_feature_set].astype('category')

# or 

for col in cat_feature_set:
    all_df[col] = all_df[col].astype('category')

all_df = pd.concat([all_df, pd.get_dummies(all_df[cat_feature_set], drop_first=True)], axis=1)
# all_df.drop([cat_feature_set], axis=1, inplace=True)

# dummy cat feature
dummy_cat = list(pd.get_dummies(all_df[cat_feature_set], drop_first=True).columns)

# numerical variables
numerical_feature_set = ['num1', 'num2']
# outcome var
outcomeVar = ['outcomeVar']

# or
numerical_feature_set =  list(set(all_df.select_dtypes('number').columns.tolist()) \
     - set(outcomeVar))

all_feature = sorted(set(dummy_cat) | set(numerical_feature_set))

all_ml_data = all_df.loc[:, all_feature + outcomeVar]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    all_ml_data[all_feature], all_ml_data[outcomeVar], test_size=0.2, stratify = all_ml_data[outcomeVar],random_state=42)

##############################################################################################


import numpy as np

from sklearn.compose import ColumnTransformer
from sklearn.datasets import fetch_openml
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.decomposition import PCA
# polynomial
from sklearn.preprocessing import PolynomialFeatures
numeric_features = ['age', 'fare']
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler()), 
    ('pca', PCA()),
    ]
)

categorical_features = ['embarked', 'sex', 'pclass']
categorical_transformer = OneHotEncoder(handle_unknown='ignore', drop='first')

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)])

# Append classifier to preprocessing pipeline.
# Now we have a full prediction pipeline.
clf_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                      ('classifier', LogisticRegression())])

param_search = {'preprocessor__num__imputer__strategy' : ['mean', 'median'],
              'preprocessor__num__pca__n_components': [5, 15, 30, 45, 60],
              'classifier__C' : [0.1, 10, 100],
              'classifier__class_weight':['balanced', {1:2},{1:5},{1:10},{1:20},{1:50}], 
              'classifier__solver' : ['liblinear', 'saga']}

param_grid = [
    {'n_estimators': [100, 150, 30], 'max_features': [2, 4, 6, 8]},
]


    # "alpha": scipy.stats.reciprocal(a=1e-7,b=1e2),
    # "beta": scipy.stats.reciprocal(a=1e-7,b=1e2),

all_feature_raw = categorical_features + numeric_features # 原始的 category 和 numerical
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    all_ml_data[all_feature_raw], all_ml_data[outcomeVar], test_size=0.2, stratify = all_ml_data[outcomeVar],random_state=42)

from sklearn.model_selection import RandomizedSearchCV
randomSearch = RandomizedSearchCV(clf_pipeline, 
    param_distributions=param_search, n_iter=50, scoring='roc_auc')
randomSearch.fit(X_train, y_train)

cvres = randomSearch.cv_results_
for mean_score, params in zip(cvres["mean_test_score"], cvres["params"]):
    print(np.sqrt(-mean_score), params)

final_model = randomSearch.best_estimator_
X_train_prepared = preprocessor.fit_transform(X_train)
X_test_prepared =  preprocessor.transform(X_test)
test_predict_class = final_model.predict(X_test_prepared) # predict class
test_predict_proba = final_model.predict_proba(X_test_prepared) # predict probabilities

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, test_predict_class)

from sklearn.metrics import precision_score, recall_score, f1_score
precision_score(y_test, test_predict_class)
recall_score(y_test, test_predict_class)
f1_score(y_test, test_predict_class)

from sklearn.metrics import precision_recall_curve
precisions, recalls, thresholds = precision_recall_curve(y_test, test_predict_proba)
import matplotlib.pyplot as plt
def plot_precision_recall_vs_threshold(precisions, recalls, thresholds):
    plt.plot(thresholds, precisions[:-1], "b--", label="Precision")
    plt.plot(thresholds, recalls[:-1], "g-", label="Recall")
    return 
plot_precision_recall_vs_threshold(precisions, recalls, thresholds)
plt.show()


from sklearn.metrics import roc_curve

fpr, tpr, thresholds = roc_curve(y_test, test_predict_proba)
def plot_roc_curve(fpr, tpr, label=None):
    plt.plot(fpr, tpr, linewidth=2, label=label)
    plt.plot([0, 1], [0, 1], 'k--') # dashed diagonal
plot_roc_curve(fpr, tpr)
plt.show()
from sklearn.metrics import roc_auc_score
roc_auc_score(y_test, test_predict_proba)

#----------------------------------------------------------------------------------------------------------#

X_train, X_test, y_train, y_test = train_test_split(
    all_ml_data[all_feature], all_ml_data[outcomeVar], test_size=0.2, stratify = all_ml_data[outcomeVar],random_state=42)
X_train, X_val, y_train, y_val = train_test_split(
    X_train[all_feature], X_train[outcomeVar], test_size=0.25, stratify = X_train[outcomeVar],random_state=42)
X_train = preprocessor.fit_transform(X_train)
X_val = preprocessor.transform(X_val)
X_test = preprocessor.transform(X_test)

from sklearn.model_selection import PredefinedSplit, GridSearchCV
split_index = [-1]*len(X_train) + [0]*len(X_val)
X = np.concatenate((X_train, X_val), axis=0)
y = np.concatenate((y_train, y_val), axis=0)
pds = PredefinedSplit(test_fold = split_index)

logistic = LogisticRegression(solver='saga', tol=1e-2, max_iter=200,
                              random_state=0)

from sklearn.utils.fixes import loguniform
from scipy.stats import uniform
distributions = dict(C=uniform(loc=0, scale=4),
                     penalty=['l2', 'l1'])

logistic = LogisticRegression(solver='saga', tol=1e-2, max_iter=200,
    random_state=0)

clf = GridSearchCV(estimator = logistic,
                   cv=pds,
                   param_grid=param_search)

# Fit with all data
clf.fit(X, y)


################################################

# Creating a dict of the models
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score
from xgboost import XGBClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_curve, auc, confusion_matrix


model_dict = {'Random Forest': RandomForestClassifier(n_estimators=200, random_state=0),
              'XGBClassifier': XGBClassifier(),
              'LogisticRegression': LogisticRegression(random_state=0),
              'K Nearest Neighbor': KNeighborsClassifier(),
              'linearSVM': LinearSVC()}

# Train test split 
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=.2,
                                                    random_state=3)

# Function to get the scores for each model in a df
from sklearn.model_selection import cross_val_predict, cross_val_score


def model_score_df(model_dict):
    model_name, ac_score_list, p_score_list, r_score_list, f1_score_list = [], [], [], [], []
    for k, v in model_dict.items():
        model_name.append(k)
        v.fit(X_train, y_train)
        y_pred = v.predict(X_test)
        # cross_val_predict(estimator, X_train, y_train, cv=3, scoring='accuracy').mean()
        # cross_val_score(estimator, X_train, y_train, cv=3, scoring='accuracy').mean()
        ac_score_list.append(accuracy_score(y_test, y_pred))
        p_score_list.append(precision_score(y_test, y_pred, average='macro'))
        r_score_list.append(recall_score(y_test, y_pred, average='macro'))
        f1_score_list.append(f1_score(y_test, y_pred, average='macro'))
    model_comparison_df = pd.DataFramea({'model_name':model_name, 'accuracy_score':ac_score_list,
        'precision_score':p_score_list, 'recall_score': r_score_list, 'f1_score':f1_score_list})
    model_comparison_df.sort_values(
        by='f1_score', ascending=False, inplace=True)
    return model_comparison_df
#########################################################
from sklearn.linear_model import SGDRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error 

########################################################
xgboost_params = { 'max_depth': [3, 5, 6, 10, 15, 20],
           'learning_rate': [0.01, 0.1, 0.2, 0.3],
           'subsample': np.arange(0.5, 1.0, 0.1),
           'colsample_bytree': np.arange(0.4, 1.0, 0.1),
           'colsample_bylevel': np.arange(0.4, 1.0, 0.1),
           'n_estimators': [100, 500, 1000]}

rf_params = {
    'bootstrap': [True],
    'max_depth': [80, 90, 100, 110],
    'max_features': [2, 4, 8, 16],
    'min_samples_leaf': [3, 4, 5],
    'min_samples_split': [8, 10, 12],
    'n_estimators': [100, 200, 300]
}
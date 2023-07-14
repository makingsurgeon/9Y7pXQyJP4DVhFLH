from sklearn import tree
import pandas as pd
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
from sklearn import metrics

def fit():
    a = pd.read_csv("data/raw/ACME-HappinessSurvey2020.csv")
    X = a.drop(["Y"], axis = 1)
    Y = a["Y"]

    clf = tree.DecisionTreeClassifier(max_depth = 2, random_state = 0)
    rfe = RFE(clf, n_features_to_select = 3)
    fit = rfe.fit(X, Y)

    X_new = X[["X1", "X5", "X6"]]

    X_train, X_test, y_train, y_test = train_test_split(
    X_new, Y, test_size=0.15, random_state=1)

    clf = clf.fit(X_train,y_train)
    y_pred = clf.predict(X_test)

    return metrics.accuracy_score(y_test, y_pred)
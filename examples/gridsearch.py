from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

cancer = load_breast_cancer()    # Get some data
X_train, X_test, y_train, y_test = train_test_split(
        cancer.data, cancer.target,
        stratify=cancer.target, random_state=1337)

tree = DecisionTreeClassifier(random_state=7331)
search_grid = {'criterion': ['gini', 'entropy'],
	'max_depth' : [5, 10, 15, 20]}

# search_grid could also be a list of dicts
search = GridSearchCV(tree, search_grid, cv=5)
search.fit(X_train, y_train)
print(search.best_params_)

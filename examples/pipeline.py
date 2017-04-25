>>> from sklearn.pipeline import Pipeline
>>> from sklearn.svm import SVC
>>> from sklearn.decomposition import PCA
>>> estimators = [('reduce_dim', PCA()), ('clf', SVC())]
>>> pipe = Pipeline(estimators)
>>> pipe 
Pipeline(steps=[('reduce_dim', PCA(copy=True, iterated_power='auto',
    n_components=None, random_state=None, svd_solver='auto', tol=0.0,
    whiten=False)), ('clf', SVC(C=1.0, cache_size=200, class_weight=None,
        coef0=0.0, decision_function_shape=None, degree=3, gamma='auto',
        kernel='rbf', max_iter=-1, probability=False, random_state=None,
        shrinking=True, tol=0.001, verbose=False))])

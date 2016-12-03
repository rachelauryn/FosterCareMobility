y  = data[1:, 0].astype(np.float)
X  = data[1:, 1:].astype(np.float)
cv = StratifiedKFold(y, n_folds = 5)

precision   = []
accuracy    = []
sensitivity = []
matthews    = []
r2          = []
f1          = []
auroc       = []
cm          = [[0, 0], [0, 0]]

for i, (train, test) in enumerate(cv):
    probas_     = rf.fit(X[train], y[train]).predict_proba(X[test])
    classes     = rf.fit(X[train], y[train]).predict(X[test])
    r2          = np.append(r2, (r2_score(y[test], probas_[:, 1])))
    precision   = np.append(precision, (precision_score(y[test], classes)))
    auroc       = np.append(auroc, (roc_auc_score(y[test], classes)))
    accuracy    = np.append(accuracy, (accuracy_score(y[test], classes)))
    sensitivity = np.append(sensitivity, (recall_score(y[test], classes)))
    f1          = np.append(f1, (f1_score(y[test], classes)))
    matthews    = np.append(matthews, (matthews_corrcoef(y[test], classes)))
    cma         = np.add(cma, (confusion_matrix(y[test], classes)))

cma         = np.array(cma)
r2          = np.array(r2)
precision   = np.array(precision)
accuracy    = np.array(accuracy)
sensitivity = np.array(sensitivity)
f1          = np.array(f1)
auroc       = np.array(auroc)
matthews    = np.array(matthews)

print("KF Accuracy: %0.2f (+/- %0.2f)" % (accuracy.mean(), accuracy.std() * 2))
print("KF Precision: %0.2f (+/- %0.2f)" % (precision.mean(), precision.std() * 2))
print("KF Sensitivity: %0.2f (+/- %0.2f)" % (sensitivity.mean(), sensitivity.std() * 2))
print("KF R^2: %0.2f (+/- %0.2f)" % (r2.mean(), r2.std() * 2))
print("KF F1: %0.2f (+/- %0.2f)" % (f1.mean(), f1.std() * 2))
print("KF AUROC: %0.2f (+/- %0.2f)" % (auroc.mean(), auroc.std() * 2))
print("KF Matthews: %0.2f (+/- %0.2f)" % (matthews.mean(), matthews.std() * 2))
print("Confusion Matrix", cma)

import sys, os, csv
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.datasets import make_classification
from sklearn.ensemble import ExtraTreesClassifier


def run_model(model):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print 'Accuracy', accuracy_score(y_test, y_pred)
    print 'Cross Val Score', cross_val_score(model, X, y)
    print 'Confusion Matrix','\n',  confusion_matrix(y_test, y_pred)
    print 'Classification Report','\n', classification_report(y_test, y_pred)


if __name__=="__main__":
    mydir='c:\datakind'
    fname='spell_clean.csv'
    #fname='providers_clean.csv'
    
    myfile=os.path.join(mydir,fname)
    df=pd.read_csv(myfile)
    
    good_val = 'GOOD'
    bad_val = 'BAD'
    unknown_val = 'UNKNOWN'
    exit_mapping = {
        'XRF':good_val, 'XLC':good_val, 'XRL':good_val, 'XCA':good_val,
        'XOT':bad_val, 'XOP':bad_val, 'XRM':bad_val, 'XRY':bad_val, 'XJP':bad_val,
        'ZTC':unknown_val, 'XUK':unknown_val
    }
    outcomes = [exit_mapping[x] for x in df.EXIT if x in exit_mapping]
    #sns.countplot(outcomes)
    df['outcome'] = outcomes
    
    hispanic_dummies = pd.get_dummies(df.HISPANIC)
    ethnic_dummies = pd.get_dummies(df.ETHNIC)
    df = pd.concat([df,hispanic_dummies], axis = 1)
    df = pd.concat([df,ethnic_dummies], axis = 1)
    relfields=['STARTAGE', 'SPELLAGE', 'N', 'U', 'Y', 
               'AN','AS','BL','MU','OT','UK','WH',
               'NPLACES','P_AL','P_FC','P_GH','P_IL',
               'P_RC','P_RT','P_SF','P_SG','P_SK','P_UK','P_KC']
    X = df[relfields]
    y = df.outcome
    
    
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    rf = RandomForestClassifier()
    run_model(rf)  
    importances=rf.feature_importances_
    
    std = np.std([tree.feature_importances_ for tree in rf.estimators_],
                 axis=0)
    indices = np.argsort(importances)[::-1]
    
    # Print the feature ranking
    print("Feature ranking:")
    relfields=np.array(relfields)
    
    for f in range(X.shape[1]):
        print("%d. feature %d %s (%f)" % (f + 1, indices[f],relfields[indices[f]], importances[indices[f]]))
    
    # Plot the feature importances of the forest
    plt.figure()
    plt.title("Feature importances")
    plt.bar(range(X.shape[1]), importances[indices],
            color="r", yerr=std[indices], align="center")
    plt.xticks(range(X.shape[1]), relfields[indices])
    plt.xlim([-1, X.shape[1]])
    plt.show()    

from numpy.core.fromnumeric import shape
from sklearn import linear_model
from sklearn.metrics import confusion_matrix,  precision_score, recall_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import make_column_transformer
import pandas as pd
from collections import Counter
from imblearn.over_sampling import SMOTE

##########################
# Data Preprocessing
##########################
def dataPreprocessing(X, y):
    '''
    for idx in range(sample_size):  #0..99999
        a = X['APR Risk of Mortality'][idx]
        if a == "Minor" or a == "Moderate" or a == "Major" or a == "Extreme":
            continue
        else:
            X['APR Risk of Mortality'][idx] = "Minor"

    dict_m = {"Minor": 1, "Moderate": 2, "Major": 3, "Extreme": 4, "nan": 0}
    X = X.replace({'APR Risk of Mortality': dict_m})
    
    #Balancing data with SMOTE
    smote = SMOTE(random_state=42)
    X, y = smote.fit_resample(X, y)
    '''
    
    #Preparationg of OHE each feature except Severity of Illness
    column_trans = make_column_transformer((OneHotEncoder(), ['APR DRG Code', 'APR Risk of Mortality',
        'CCS Diagnosis Code', 'CCS Procedure Code', 'APR MDC Code']), remainder='passthrough')
    
    #One Hot Encoding Features 
    X = column_trans.fit_transform(X)
    
    #Making training/testing classes
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)


    return X_train, y_train, X_test, y_test


#################################
# Grouping LOS for classification
#################################
def grouping(sample_size, y, grp): 
    for i in range(sample_size): 
        value = y[i] 
        if value < grp[0]:
            y[i] = 0
        #Uncomment two lines below to test 3 groups
        elif value <grp[1]:
            y[i] = 1
        else:
            y[i] = 2


    from collections import Counter
    print(Counter(y)) #Uncomment if you want to see how many values in each group
    return y

##############
# Drop By Frequency
# This method deletes rows based on the frequency of the values in that feature
# i.e. Drop rows where the occurence of the specific value is less than some number
#############
def dropByFrequency(df, col, limit):
    print("Dropping values at", col, "with occurences less than", limit)
    val_Count = Counter(df[col])
    for i in df[col].index:
        #print("At index:", i, " with value ", df.at[i, 'APR DRG Code'])
        
        if val_Count[df.at[i, col]] < limit:
            try:
                df.drop([i], inplace=True) 
                
                #print("Dropped", df.index[i]) #df.at[i,'APR DRG Code']) Throws IndexError
            except IndexError:
                print("i as", i, "is broken")
    #print(df[col].values)
    df = df.reset_index(drop=True) #(Necessary?)
    print(col, "cleaned")
    return df

##############
# Replace By Frequency
# This method replaces and "combines" values based on the frequency of that value in the df
# e.g. If APR DRG Code 123, 567, and 476 only occur less than some number of times, replace instances of 123, 567, and 476 with 999.
#############
def replaceByFrequency(df, col, limit, replacement):
    print("Assigning values at", col, "with occurences less than", limit, "to", replacement)
    val_Count = Counter(df[col])
    for i in df[col].index:
        #print("At index:", i, " with value ", df.at[i, 'APR DRG Code'])
        
        if val_Count[df.at[i, col]] < limit:
            try:
               df.at[i,col] = replacement
                #print("Dropped", df.index[i]) #df.at[i,'APR DRG Code']) Throws IndexError
            except IndexError:
                print("i as", i, "is broken")
    #print(df[col].values)
    df = df.reset_index(drop=True) #(Necessary?)
    print(col, "cleaned")
    return df

###################
# Logistic Regression
###################
def logisticRegression(X_train, y_train, X_test, y_test):
    from sklearn.linear_model import LogisticRegression

    clf = LogisticRegression(class_weight='balanced',
                                 multi_class='ovr', max_iter=1000)
    clf.fit(X_train, y_train)
    results("## Logistic Regression ##", clf, X_test, y_test)
    ## plotConfMat(clf, X_test, y_test)


###################
# Decision Tree
###################
def decisionTree(X_train, y_train, X_test, y_test):
    from sklearn import tree

    clf = tree.DecisionTreeClassifier(class_weight='balanced')
    clf = clf.fit(X_train, y_train)

    results("## Decision Tree ##", clf, X_test, y_test)
    ### plotConfMat(clf, X_test, y_test)
    ## plot not working
    #tree.plot_tree(clf)


#########################################
# Random Forest
#########################################
def randomForest(X_train, y_train, X_test, y_test):
    from sklearn.ensemble import RandomForestClassifier

    clf = RandomForestClassifier(n_estimators=200, class_weight='balanced')
    clf = clf.fit(X_train, y_train)

    results("## Random Forest ##", clf, X_test, y_test)
    ### plotConfMat(clf, X_test, y_test)

#########################################
# Gradient Boosting Classifier
#########################################
def gradientBoosting(X_train, y_train, X_test, y_test):
    from sklearn.ensemble import GradientBoostingClassifier

    clf = GradientBoostingClassifier(n_estimators=200, learning_rate=1.0,
           max_depth=1, random_state=0).fit(X_train, y_train)

    results("## Gradient Boosting Classifier ##", clf, X_test, y_test)
    ### plotConfMat(clf, X_test, y_test)
    # 0.57455

###################
# Ada Boost
###################
def AdaBoost(X_train, y_train, X_test, y_test):
    from sklearn.ensemble import AdaBoostClassifier
    from sklearn.datasets import make_classification
    X, y = make_classification(n_samples = 1000, n_features = 10,n_informative = 2, n_redundant = 0,random_state = 0, shuffle = False)
    ADBclf = AdaBoostClassifier(n_estimators = 100, random_state = 0)
    ADBclf.fit(X_train, y_train)
    results("## AdaBoost Classifier ##", ADBclf, X_test, y_test)

###################
# MLP Classifier
###################
def MLPClassifier(X, y):
    from sklearn.neural_network import MLPClassifier
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y,
                            random_state=1)
    clf = MLPClassifier(solver='adam', alpha=1e-5, hidden_layer_sizes=(5, 2),
                    random_state=1, max_iter=100)
    clf.fit(X_train, y_train)

    #print(clf.predict_proba(X_test[:5]))
    #print(y_test[:20])
    #print(clf.predict(X_test[:20]))
    results("## MLP Classifier ##", clf, X_test, y_test)
    # plotConfMat(clf, X_test, y_test)


#########################
# Classification Results
########################
def results(str, clf, X_test, y_test):
    print("\n"+str)
    print("Accuracy: ", clf.score(X_test, y_test))
    y_pred = clf.predict(X_test)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')

    F1 = 2 * (precision * recall) / (precision + recall)
    print("Precision: ", precision)
    print("Recall: ", recall)
    print("F1: ", F1)
    print(confusion_matrix(y_test, y_pred))
    
#########################
# Plot Normalized Confusion Matrix
########################
def plotConfMat(clf, X_test, y_test):
    import matplotlib.pyplot as plt
    from sklearn.metrics import plot_confusion_matrix
    plot_confusion_matrix(clf, X_test, y_test,
                          #cmap=plt.cm.cmap_d,
                          normalize='true')
    plt.show()

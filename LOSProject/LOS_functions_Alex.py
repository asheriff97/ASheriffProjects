from sklearn import linear_model
from sklearn.metrics import confusion_matrix
from collections import Counter

##########################
# Data Preprocessing
##########################
def dataPreprocessing(sample_size, training_size, X, y):

     # convert the value of Age Group to numbers
    dict = {"0 to 17": 1, "18 to 29": 2, "30 to 49": 3, "50 to 69": 4, "70 or Older": 5}
    X = X.replace({'Age Group': dict})

    # convert the value of Genders to numbers
    dict_g = {"M": 1, "F": 2, "U": 0}
    #g = v.fit_transform(dict_g)
    X = X.replace({'Gender': dict_g})

    # convert the value of Type of Admission to numbers
    dict_t = {'Elective': 1, 'Emergency': 2, 'Newborn': 3, 'Not Available': 4, 'Trauma': 5, 'Urgent': 6}
    #t = v.fit_transform(dict_t)
    X = X.replace({'Type of Admission': dict_t})
    
    # convert the value of APR Risk of Mortality to   numbers
    for idx in range(sample_size):  #0..99999
        a = X['APR Risk of Mortality'][idx]
        if a == "Minor" or a == "Moderate" or a == "Major" or a == "Extreme":
            continue
        else:
            X['APR Risk of Mortality'][idx] = "Minor"

    dict_m = {"Minor": 1, "Moderate": 2, "Major": 3, "Extreme": 4, "nan": 0}
    X = X.replace({'APR Risk of Mortality': dict_m})
    

    # convert the value of Race to numbers
    dict_r = {"White": 1, "Other Race": 2, "Black/African American": 3, "Multi-racial": 4}
    X = X.replace({'Race': dict_r})

    #convert the value of Ethnicity to numbers
    dict_e = {"Not Span/Hispanic": 1, "Spanish/Hispanic": 2, "Unknown": 3, "Multi-ethnic": 4}
    X = X.replace({'Ethnicity': dict_e})

    #convert the value of Patient Disposition to numbers
    dict_d = {"Home or Self Care": 1, "Hosp Basd Medicare Approved Swing Bed": 2, "Short-term Hospital": 3, "Facility w/ Custodial/Supportive Care": 4, "Skilled Nursing Home": 5,
                "Expired": 6, "Home w/ Home Health Services": 7, "Hospice - Home": 8, "Inpatient Rehabilitation Facility": 9, "Left Against Medical Advice": 10, "Psychiatric Hospital or Unit of Hosp": 11,
                "Federal Health Care Facility": 12, "Cancer Center or Children's Hospital": 13, "Hospice - Medical Facility": 14, "Medicare Cert Long Term Care Hospital": 15,
                "Court/Law Enforcement": 16, "Another Type Not Listed": 17, "Critical Access Hospital": 18, "Medicaid Cert Nursing Facility": 19}
    X = X.replace({'Patient Disposition': dict_d})

    #convert the value of APR Medical Surgical Description to numbers
    dict_a = {"Medical": 1, "Surgical": 2, "Not Applicable": 3}
    X = X.replace({"APR Medical Surgical Description": dict_a})         

    #convert the value of Emergency Department Indicator to numbers
    dict_b = {"Y": 1, "N": 2}
    X = X.replace({"Emergency Department Indicator": dict_b}) 


    # split data for training and testing
    X_train = X[:training_size]
    X_test = X[training_size:]
    y_train = y[:training_size]
    y_test = y[training_size:]

    # data normalization
    mean = X_train.mean(axis=0)
    std = X_train.std(axis=0)
    X_train -= mean
    X_train /= std
    X_test -= mean
    X_test /= std

    return X, y, X_train, y_train, X_test, y_test


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


    #from collections import Counter
    print("Unbalanced")
    print(Counter(y))
    return y

###################
# Logistic Regression
###################
def logisticRegression(X_train, y_train, X_test, y_test):
    from sklearn.linear_model import LogisticRegression

    clf = LogisticRegression(class_weight='balanced',
                                 multi_class='ovr')
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

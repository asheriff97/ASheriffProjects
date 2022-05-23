#####################################3
# Length of Stay (LOS) in hospital
# Alex's Balanced Data Sets W/ Optimal Features
#####################################

import LOS_functions
import pandas # to read csv file (comma separated values)
import numpy as np

#### read csv file with Pandas
#selected columns
selcols = ['APR DRG Code',  'APR Severity of Illness Code', 'APR Risk of Mortality',  
            'CCS Diagnosis Code', 'CCS Procedure Code', 'APR MDC Code', 'Length of Stay']


sample_size=200000
training_size=int(0.8*sample_size)


df=pandas.read_csv("LOS200k.csv", usecols=selcols, nrows=sample_size)    #df -data frame


#target -- LOS
y = df['Length of Stay'].replace("120 +", 120)

print("original sample size:", df.shape[0])

#print(y.value_counts().shape)
y = np.array(y).astype("float32")


### drop samples in which LOS>bad
bad = 15
df.drop(df[(y > bad)].index, inplace=True)
df = df.reset_index(drop=True)
y = y[y<=bad]
print("sample size after dropping LOS > 15 : ", df.shape[0])

#features
X=df[['APR DRG Code', 'APR Severity of Illness Code', 'APR Risk of Mortality',
        'CCS Diagnosis Code', 'CCS Procedure Code', 'APR MDC Code']]

X, y, X_train, y_train, X_test, y_test = LOS_functions.dataPreprocessing(
    df.shape[0], training_size, X, y)


print("\n-------Training and testing results-------")

grp = [4,8]

#To switch from 2 to 3 groups open LOS_functions.py and see grouping def
LOS_functions.grouping(df.shape[0], y, grp)


#LOS_functions.logisticRegression(X_train, y_train, X_test, y_test)
#for x in range(5):
#    LOS_functions.decisionTree(X_train, y_train, X_test, y_test)
#for x in range(5):
LOS_functions.randomForest(X_train, y_train, X_test, y_test)
#LOS_functions.gradientBoosting(X_train, y_train, X_test, y_test)
#LOS_functions.AdaBoost(X_train, y_train, X_test, y_test)



from collections import Counter
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler, SMOTE, KMeansSMOTE

'''
#UNDERSAMPLING START
undersample = RandomUnderSampler(sampling_strategy='not minority')
X_over, y_over = undersample.fit_resample(X_train, y_train)
print("\nUndersampled Training Data")
print(Counter(y_over))

X_testOver, y_testOver = undersample.fit_resample(X_test, y_test)
print("\nUndersampled Testing Data")
print(Counter(y_testOver))

LOS_functions.logisticRegression(X_over, y_over, X_testOver, y_testOver)
#for x in range(5):
#LOS_functions.decisionTree(X_over, y_over, X_testOver, y_testOver)
#for x in range(5):
#LOS_functions.randomForest(X_over, y_over, X_testOver, y_testOver)
LOS_functions.gradientBoosting(X_over, y_over, X_testOver, y_testOver)
LOS_functions.AdaBoost(X_over, y_over, X_testOver, y_testOver)
#UNDERSAMPLING END
'''

'''
#RANDOMOVERSAMPLING START
oversample = RandomOverSampler(sampling_strategy='not majority')
X_under, y_under = oversample.fit_resample(X_train,y_train)
print("Oversampled Training Data")
print(Counter(y_under))

X_testUnder, y_testUnder = oversample.fit_resample(X_test, y_test)
print("Oversampled Testing Data")
print(Counter(y_testUnder))

LOS_functions.logisticRegression(X_under, y_under, X_testUnder, y_testUnder) 
#LOS_functions.decisionTree(X_under, y_under, X_testUnder, y_testUnder)
#for x in range(5):
#LOS_functions.randomForest(X_under, y_under, X_testUnder, y_testUnder)
LOS_functions.gradientBoosting(X_under, y_under, X_testUnder, y_testUnder)
LOS_functions.AdaBoost(X_under, y_under, X_testUnder, y_testUnder)
#RANDOMOVERSAMPLING END
'''

'''
#SMOTE START
smote = SMOTE(random_state=42)
X_smote, y_smote = smote.fit_resample(X_train, y_train)
print("SMOTE Training Data")
print(Counter(y_smote))

X_testSmote, y_testSmote = smote.fit_resample(X_test, y_test)
print("SMOTE Testing Data")
print(Counter(y_testSmote))

#LOS_functions.logisticRegression(X_smote, y_smote, X_testSmote, y_testSmote) 
#for x in range(5):
#LOS_functions.decisionTree(X_smote, y_smote, X_testSmote, y_testSmote)
#for x in range(5):
#LOS_functions.randomForest(X_smote, y_smote, X_testSmote, y_testSmote)
LOS_functions.gradientBoosting(X_smote, y_smote, X_testSmote, y_testSmote)
LOS_functions.AdaBoost(X_smote, y_smote, X_testSmote, y_testSmote)
#SMOTE END
'''




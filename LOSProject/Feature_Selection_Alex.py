#####################################3
# TEST FEATURE SELECTION
# This file tests the relationship between the Length of Stay feature and other listed features.
# Based on https://machinelearningmastery.com/feature-selection-machine-learning-python/
#####################################


import LOS_functions_Alex
import pandas # to read csv file (comma separated values)
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

#### read csv file with Pandas
#selected columns
selcols = ['APR DRG Code','APR Severity of Illness Code', 'CCS Diagnosis Code', 'Age Group', 'APR Medical Surgical Description', 'Emergency Department Indicator',
         'Gender','APR Risk of Mortality','Type of Admission', 'Race', 'Ethnicity', 'Patient Disposition', 'CCS Procedure Code', 'APR MDC Code', 'Length of Stay']


sample_size=200000
training_size=int(0.8*sample_size)

df=pandas.read_csv("LOS200k.csv", usecols=selcols, nrows=sample_size)    #df -data frame

#target -- LOS
y = df['Length of Stay'].replace("120 +", 120)

print("original sample size:", df.shape[0])

#print(y.value_counts().shape)
y = np.array(y).astype("float32")

#features
X=df[['APR DRG Code','APR Severity of Illness Code', 'CCS Diagnosis Code', 'Age Group',
         'Gender','APR Risk of Mortality','Type of Admission', 'Race', 'Ethnicity', 'Patient Disposition', 
         'CCS Procedure Code', 'APR MDC Code', 'Emergency Department Indicator']]

X, y, X_train, y_train, X_test, y_test = LOS_functions_Alex.dataPreprocessing(
    sample_size, training_size, X, y)

#Feature Selection
test = SelectKBest(score_func=chi2, k=4)
fit = test.fit(X, y)

np.set_printoptions(precision=3)
print(fit.scores_) #The higher the score the higher correlation with LOS... I.e. we should include it for training/testing

features = fit.transform(X)

print(features[0:5,:])




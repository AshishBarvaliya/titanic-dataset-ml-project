import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import missingno
import seaborn as sns
plt.style.use('seaborn-whitegrid')

#import data
train = pd.read_csv("train.csv")
test=pd.read_csv("test.csv")

missingno.matrix(train,figsize=(10,7))

# How many people survived?
fig = plt.figure(figsize=(10,1))
sns.countplot(y='Survived', data=train);
print(train.Survived.value_counts())

# one by one column exploration and visulisation and ckeck correlation
#sns.distplot(train.Pclass)
#corr = train.corrwith(train.Survived)
#ax = sns.heatmap(corr,square=True)

X_train = train.drop(['Survived','PassengerId','Name'], axis=1)
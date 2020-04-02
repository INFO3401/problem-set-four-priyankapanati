# Problem 1:

import pandas as pd
import matplotlib.pyplot as plt


def loadAndCleanData(data):
    data = pd.read_csv(data)
    newData=data.fillna("0")
    print(newData)
    return newData
#def helloWorld():
    #print("Hello, World")
def computePDF(feature,DataFrame):
    s = DataFrame[feature].plot.kde()
    plt.show()
def viewDistribution(feature, dataFrame):
    dataFrame.hist(column=feature)
    plt.show()
def viewLogDistribution(feature, dataFrame):
    dataFrame.hist(column=feature,log=True)
    plt.show()
#Problem 7
#Three bins for age are: 0-40,40-80,80-120
#print probability someone is between 0 and 40
def computeProbability(feature,bin,data):
    #count how many data points are between 0and 40
    #count total data points
    count=0.0
    for i,dataPoints in data.iterrows():
        if dataPoints[feature]>=bin[0] and dataPoints[feature]<bin[1]:
            count+=1
    totalData=len(data)
    probability=count/totalData
    return probability
#Problem 8
def computeDefaultRisk(column,feature,bin,data):
    count=0.0
    count2=0.0
    for i,dataPoints in data.iterrows():
        if dataPoints[feature]>=bin[0] and dataPoints[feature]<bin[1]:
            count+=1
            if dataPoints[column]==1:
                count2+=1
    totalData=len(data)
    #bayes theorem
    probability=count/totalData
    probability2=count2/totalData
    print(probability2/probability)
    return probability2/probability
#problem 9
#problem 10
def problem11 (df):
    dfNew=loadAndCleanData("newLoans.csv")

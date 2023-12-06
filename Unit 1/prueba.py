import pandas as pd
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split


dataset = pd.read_csv(r'C:\Users\Axel Esdras\Desktop\machine\Social_Network_Ads.csv', sep=",")


dataset = dataset.drop(columns="User ID")


dataset["Male"] = (dataset["Gender"] == "Male").astype(int)
dataset["Female"] = (dataset["Gender"] == "Female").astype(int)


dataset = dataset.drop(columns="Gender")

column_order = list(dataset.columns.difference(["Purchased"])) + ["Male", "Female"] + ["Purchased"]
dataset = dataset[column_order]

X = dataset.drop(columns="Purchased")
y = dataset["Purchased"]


from sklearn.linear_model import Perceptron

xtrain = dataset.iloc[:319, 0:4]
ytrain = dataset.iloc[:319, 4]
xtest = dataset.iloc[320:, 0:4]
ytest = dataset.iloc[320:, 4]

# print(xtrain.head(1))
# print(ytrain.head(1))
# print(xtest.head(1))
# print(ytest.head(1))

clf = Perceptron(tol=1e-3, random_state=0)
clf.fit(xtrain, ytrain)
Perceptron()
print(dataset.head(10))
print("Score train is =" ,clf.score(xtrain, ytrain))
print("Score test is =" , clf.score(xtest, ytest))
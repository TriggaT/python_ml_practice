from sklearn import datasets

iris = datasets.load_iris()

# print(iris)

features = iris.data
labels = iris.target

# print(features)
print(labels)

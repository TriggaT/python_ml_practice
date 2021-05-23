from sklearn import datasets
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()

# print(iris)

features = iris.data
labels = iris.target

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=.5)

print(features_train)

# print(features)
# print(labels)

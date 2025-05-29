from sklearn.tree import DecisionTreeClassifier

X = [[0, 0], [1, 1], [0, 1], [1, 0]]
y = [0, 1, 1, 0]

model = DecisionTreeClassifier()
model.fit(X, y)

print("Prediction for [1, 1]:", model.predict([[1, 1]]))

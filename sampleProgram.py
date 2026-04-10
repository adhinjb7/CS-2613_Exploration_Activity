# IMPORTING LIBRARIES
from sklearn.datasets import load_diabetes, load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import mean_squared_error, accuracy_score

# REGRESSION TESTING (Diabetes Dataset)
print("----- REGRESSION: Linear Regression -----")

diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

reg_model = LinearRegression()
reg_model.fit(X_train, y_train)

reg_predictions = reg_model.predict(X_test)

mse = mean_squared_error(y_test, reg_predictions)
print("Mean Squared Error:", mse)

sample_reg = [X_test[0]]
print("Sample Prediction:", reg_model.predict(sample_reg)[0])

# DECISION TREE CLASSIFIER (Iris Dataset)
print("\n----- CLASSIFICATION: Decision Tree -----")

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

dt_model = DecisionTreeClassifier()
dt_model.fit(X_train, y_train)

dt_predictions = dt_model.predict(X_test)

dt_accuracy = accuracy_score(y_test, dt_predictions)
print("Decision Tree Accuracy:", dt_accuracy)

sample_dt = [X_test[0]]
print("Sample Prediction (class):", dt_model.predict(sample_dt)[0])



# MLP CLASSIFIER (Iris Dataset)

print("\n----- CLASSIFICATION: MLP Classifier -----")

mlp_model = MLPClassifier(max_iter=1000)
mlp_model.fit(X_train, y_train)

mlp_predictions = mlp_model.predict(X_test)

mlp_accuracy = accuracy_score(y_test, mlp_predictions)
print("MLP Accuracy:", mlp_accuracy)

sample_mlp = [X_test[1]]
print("Sample Prediction (class):", mlp_model.predict(sample_mlp)[0])

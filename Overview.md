# Scikit-learn Package Overview

## 1. Which package/library did you select?

The package selected for this project is **Scikit-learn**, a widely used open-source machine learning library in Python.

## 2. What is the package/library?

Scikit-learn is a powerful Python library designed for machine learning, data analysis, and predictive modeling. It provides tools to build, train, and evaluate models efficiently.

### Purpose

The main purpose of Scikit-learn is to simplify machine learning by providing ready-to-use algorithms for:

- Regression (predicting continuous values)
- Classification (predicting categories)
- Data preprocessing
- Model evaluation
  
### How do you use it?

Scikit-learn follows a structured workflow:

1. Import libraries  
2. Load dataset  
3. Split data  
4. Train model  
5. Make predictions  
6. Evaluate results  

### Example

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

data = load_iris()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
```

## 3. What are the functionalities of the package/library?

Scikit-learn provides several key functionalities used in this project:

### Regression Testing (Linaer Regression)

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

### Decision Tree Classifier

```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

### MLP Classifier

```python
from sklearn.neural_network import MLPClassifier

model = MLPClassifier(max_iter=1000)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

### Data Spliting

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```

### Model Evaluation

```python
from sklearn.metrics import mean_squared_error, accuracy_score

mse = mean_squared_error(y_test, predictions)
accuracy = accuracy_score(y_test, predictions)
```

## 4. When was it created?

It was originally called scikits.learn and was initially developed by David Cournapeau as a Google summer of code project in 2007. Later, in 2010, Fabian Pedregosa, Gael Varoquaux, Alexandre Gramfort, and Vincent Michel, from FIRCA (French Institute for Research in Computer Science and Automation), took this project at another level and made the first public release (v0.1 beta) on 1st Feb. 2010.

## 5. Why did you select this package/library?

I selected Scikit-learn because it provides practical tools for implementing machine learning models such as regression, decision trees, and neural networks.

It is widely used in both academic and industry environments, making it valuable to learn. Additionally, its simple and consistent design makes it easier to understand complex machine learning concepts.

## 6. How did learning the package/library influence your learning of the language?

Learning Scikit-learn improved my understanding of Python by showing how the language can be used for real-world applications such as machine learning and data analysis.

It helped me learn:

- How to work with datasets
- How to use external libraries
- How to structure programs logically
- How to apply algorithms in practice

## 7. How was your overall experience with the package/library?

Overall, my experience with Scikit-learn was very positive.

- It is easy to use
- Well-documented
- Powerful and efficient

### When would you recommend this package/library?

I would recommend Scikit-learn to:

- Beginners learning machine learning
- Students working on data projects
- Developers interested in AI
- Would you continue using this package/library? Why or why not?

I would also continue using Scikit-learn because:

- It provides reliable tools
- It supports many algorithms
- It integrates well with other Python libraries


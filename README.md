# CS-2613_Exploration_Activity

## Which package/library does the sample program demonstrate?

The package/library demonstrated in this project is **Scikit-learn**, a widely used open-source machine learning library in Python.

Scikit-learn provides simple and efficient tools for data analysis, data mining, and predictive modeling. It is designed to be easy to use while still offering powerful functionality. The library is built on top of other core Python scientific libraries such as NumPy, SciPy, and Matplotlib which allow it to perform numerical computations and data visualization efficiently.

In this project, Scikit-learn is used to implement multiple machine learning models, including:

- Linear Regression (for predicting continuous values)
- Decision Tree Classifier (for classification tasks)
- MLP Classifier (a neural network model)

## How does someone run your program?

To run this program, the user must have Python installed on their system along with the required libraries.

### Step 1: Install Required Libraries

Open a terminal or command prompt and install the necessary dependencies using pip:

pip install scikit-learn pandas

### Step 2: Download or Clone the Repository

Download the project files or clone the repository using Git 

git clone <repository-link>
cd CS-2613_Exploration_Activity

### Step 3: Run the Program

python sampleProgram.py

### Step 4: Output

The program will display results in the console, including:

- Mean Squared Error (for regression)
- Accuracy scores (for classifiers)
- Sample predictions

## 3. What purpose does your program serve?

The purpose of this program is to demonstrate how machine learning can be used to analyze real-world data and make predictions using different models.

This program applies three key machine learning techniques:

- **Linear Regression** on the diabetes dataset to predict disease progression (continuous values)
- **Decision Tree Classification** on the iris dataset to classify data into categories
- **MLP Classifier (Neural Network)** to perform more advanced classification

The program serves several important purposes:

- Demonstrates how to load and work with real-world datasets
- Shows how to split data into training and testing sets
- Illustrates how different machine learning models are trained
- Compares multiple algorithms within the same program
- Evaluates model performance using metrics such as Mean Squared Error and Accuracy

Overall, this program simulates a realistic data science workflow where data is processed, models are trained, predictions are made, and results are evaluated.

## What would be some sample input/output?

### Sample Input

The program primarily uses a built-in dataset, so the input consists of numerical feature values representing patient data. These values are handled internally by the program.

Each value represents a normalized feature such as age, BMI, or blood pressure (for the diabetes dataset), or measurements like petal length and width (for the iris dataset).

A sample output would look like this:

<img width="351" height="197" alt="image" src="https://github.com/user-attachments/assets/735a1676-d265-4341-b537-06985565ee5a" />




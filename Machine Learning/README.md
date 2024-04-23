# Machine Learning Projects

This repository contains two machine learning projects implemented in Python. The first project is an Exam Grade Prediction model, and the second project is a Neural Network implementation from scratch.

## 1. Exam Grade Prediction

This project aims to predict a student's exam grade based on their study time and TV time. It employs a multiple linear regression model to find the relationship between the input variables (study time and TV time) and the output variable (exam grade).

### Features

- Generates realistic data for training and testing the model
- Implements gradient descent algorithm to optimize the model parameters
- Visualizes the data and the fitted model in a 3D scatter plot

### Usage

1. Run the Python script to generate the realistic data and save it to a CSV file.
2. The script will train the model using gradient descent and print the optimized parameters.
3. Finally, the script will plot the data and the fitted model in a 3D scatter plot.

### Dependencies

- pandas
- matplotlib
- mpl_toolkits
- csv
- random
- numpy

## 2. Neural Network from Scratch

This project implements a basic neural network from scratch using NumPy. The neural network consists of two dense layers, a ReLU activation function, and a softmax activation function for the output layer. The project uses the spiral dataset from the NNFS (Neural Network from Scratch) library.

### Features

- Implements dense layers, ReLU activation, and softmax activation from scratch
- Utilizes the spiral dataset for training and testing
- Calculates the categorical cross-entropy loss

### Usage

1. Run the Python script to create and train the neural network on the spiral dataset.
2. The script will print the predicted output of the first five samples and the calculated loss.

### Dependencies

- numpy
- nnfs (Neural Network from Scratch library)

### Note

Please note that the second project (Neural Network from Scratch) is not fully completed and may require additional modifications or improvements.

## Contributing

Contributions to these projects are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

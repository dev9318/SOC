from random import random


# Make a prediction with weights
def predict_train(row, weights):
    activation = weights[0]
    for i in range(len(row)-1):
    	activation += weights[i + 1] * row[i]
    return 1.0 if activation >= 0.0 else 0.0


def predict_test(row, weights):
    activation = weights[0]
    for i in range(len(row)):
    	activation += weights[i + 1] * row[i]
    return 1.0 if activation >= 0.0 else 0.0

# Estimate Perceptron weights using stochastic gradient descent
def train_weights(train, l_rate, n_epoch):
    weights = [random() for i in range(len(train[0]))]
    for epoch in range(n_epoch):
        for row in train:
            prediction = predict_train(row, weights)
            error = row[-1] - prediction
            weights[0] = weights[0] + l_rate * error
            for i in range(len(row)-1):
                weights[i + 1] = weights[i + 1] + l_rate * error * row[i]
    return weights

#training data
dataset = [[1,0,1,1],[0,0,1,0],[1,1,0,1],[1,1,1,1]]
l_rate = 0.05
n_epoch = 10
weights = train_weights(dataset, l_rate, n_epoch)

#input
n = int(input("How many predictions would you like to make\n"))
for _ in range(n):
    data_column = [int(x) for x in input().split()]
    print(predict_test(data_column,weights))

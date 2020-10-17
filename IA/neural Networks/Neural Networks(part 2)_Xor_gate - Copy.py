import numpy as np
import matplotlib.pyplot as plt


#required to predit a numbert between 0 and 1
def sigmoid (x):
    return 1/(1 + np.exp(-x))

#required for back propagation
def sigmoid_derivative(x):
    return x * (1 - x)

datai=[]
datao=[]
for i in range(10):
    for j in range(10):
        datai.append([i,j])
        datao.append((i+1)*(j+1))

#making data for training it
inputs = (datai)
expected_output = (datao)


epochs = 4000
lr = 0.

#making random weights and bias

hidden_weights = np.random.uniform(size=(2,2))
hidden_bias =np.random.uniform(size=(1,2))
output_weights = np.random.uniform(size=(2,1))
output_bias = np.random.uniform(size=(1,1))

errors=[]
x=[]
y=[]
x1=[]

    
#Training algorithm executing the algorithm 10000 times
for i in range(epochs):
    
        
    for i in range(len(expected_output)):
        #Forward Propagation
        #1st layer
        hidden_layer_activation = np.dot(np.array(inputs[i]),hidden_weights)
        hidden_layer_activation = hidden_layer_activation + hidden_bias
        hidden_layer_output = sigmoid(hidden_layer_activation)

        # 2nd layer (using the output of the previous layer as input)
        output_layer_activation = np.dot(hidden_layer_output,output_weights)
        output_layer_activation = output_layer_activation + output_bias
        predicted_output = sigmoid(output_layer_activation)


        #Backpropagation
        #2nd layer
        error = np.array(expected_output[i]) - predicted_output
        d_predicted_output = error * sigmoid_derivative(predicted_output)

        #1st layer
        error_hidden_layer = d_predicted_output.dot(output_weights.T)
        d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)
	

        #Updating Weights and Biases
        output_weights =output_weights + hidden_layer_output.T.dot(d_predicted_output) * lr
        output_bias = output_bias + np.sum(d_predicted_output,axis=0,keepdims=True) * lr
        hidden_weights = hidden_weights + np.array(inputs[i]).T.dot(d_hidden_layer.T) * lr
        hidden_bias = hidden_bias + np.sum(d_hidden_layer,axis=0,keepdims=True) * lr
    

hidden_layer_activation = np.dot([10,10],hidden_weights)
hidden_layer_activation = hidden_layer_activation + hidden_bias
hidden_layer_output = (hidden_layer_activation)

        # 2nd layer (using the output of the previous layer as input)
output_layer_activation = np.dot(hidden_layer_output,output_weights)
output_layer_activation = output_layer_activation + output_bias
predicted_output = (output_layer_activation)


print(predicted_output)


from NN.NeuralNetwork import NeuralNetwork
from NN.NeuronLayer import NeuronLayer


def main():
    layer2 = NeuronLayer(1, 1, weights=[[0.3]], biases=[0.4])
    layer1 = NeuronLayer(1, 2, nextLayer=layer2, weights=[[0.4, 0.3]], biases=[0.5])
    layer2.setPreviousLayer(layer1)
    
    nn = NeuralNetwork([1],0)
    nn.setFirstLayer(layer1)
    nn.setOutputLayer(layer2)    
    nn.train([1, 1], [1])

    n = layer1.neurons[0]
    print(n.bias)
    print(n.weights)
    n = layer2.neurons[0]
    print(n.bias)
    print(n.weights)

main()

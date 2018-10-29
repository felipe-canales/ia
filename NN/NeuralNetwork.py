from NN.Sigmoid import Sigmoid as Neuron
from NN.NeuronLayer import NeuronLayer

class NeuralNetwork:
    def __init__(self, layers, inputs):
        layers.insert(0, inputs)
        last = layers.pop()
        self.outputLayer = NeuronLayer(last, layers[-1])

        lastLayer = self.outputLayer
        last = layers.pop()
        while len(layers) > 0:
            currentLayer = NeuronLayer(last, layers[-1], lastLayer)
            lastLayer.setPreviousLayer(currentLayer)
            last = layers.pop()
            lastLayer = currentLayer
        self.firstLayer = lastLayer

    def setFirstLayer(self, layer):
        self.firstLayer = layer

    def setOutputLayer(self, layer):
        self.outputLayer = layer

    def feed(self, inputs):
        return self.firstLayer.feed(inputs)

    def train(self, inputs, expected, learningRate = 0.5):
        result = self.feed(inputs)
        self.outputLayer.propagate(expected)
        self.firstLayer.learn(inputs, learningRate)
        return result

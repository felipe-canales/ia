from NN.Perceptron import Perceptron
import math

class Sigmoid(Perceptron):
    def __init__(self, inputs,\
                 bias = None, weights = None, learningRate = None):
        super(Sigmoid, self).__init__(inputs, bias, weights, learningRate)
        self.delta = 0
        self.output = None

    def feed(self, inputs):
        suma = 0
        for i in range(len(self.weights)):
            suma += inputs[i] * self.weights[i]
        suma += self.bias
        self.output = 1 / (1.0 + math.exp(-suma))
        return self.output

    def getOutput(self):
        return self.output

    def getError(self, i):
        return self.weights[i] * self.delta

    def adjustDelta(self, error):
        self.delta = error * (self.output * (1 - self.output))

    def learn(self, inputs, learningRate = None):
        if learningRate == None:
            learningRate = self.lr
        self.bias += learningRate * self.delta
        for i in range(len(self.weights)):
            self.weights[i] += learningRate * self.delta * inputs[i]

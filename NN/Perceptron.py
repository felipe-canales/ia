import random

class Perceptron(object):
    def __init__(self, inputs,\
                 bias = None, weights = None, learningRate = 0):
        self.lr = learningRate
        mult = [-1, 1]
        if bias != None:
            self.bias = bias
        else:
            self.bias = random.uniform(0.5, 2.0) * mult[random.randint(0,1)]
        if weights != None:
            self.weights = weights
        else:
            self.weights = [random.uniform(-2.0, 2.0) * mult[random.randint(0,1)] \
                            for _ in range(inputs)]

    def feed(self, inputs):
        suma = 0
        for i in range(len(self.weights)):
            suma += inputs[i] * self.weights[i]
        if suma + self.bias > 0:
            return 1
        else: return 0

    def train(self, inputs, expected, learningRate = None):
        if learningRate == None:
            learningRate = self.lr
        result = self.feed(inputs)
        diff = expected - result
        for i in range(len(inputs)):
            self.weights[i] += learningRate * inputs[i] * diff
        self.bias += learningRate * diff
        return result
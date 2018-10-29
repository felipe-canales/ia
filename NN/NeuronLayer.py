from NN.Sigmoid import Sigmoid as Neuron

class NeuronLayer:
    def __init__(self, neuronNumber, inputNumber, nextLayer = None, weights = None, biases = None):
        if biases == None:
            self.neurons = [Neuron(inputNumber) for _ in range(neuronNumber)]
        else:
            self.neurons = []
            for i in range(neuronNumber):
                self.neurons.append(Neuron(inputNumber, biases[i], weights[i]))
        self.outputs = []
        self.next = nextLayer
        self.prev = None

    def setPreviousLayer(self, layer):
        self.prev = layer
    
    def feed(self, inputs):
        self.outputs = []
        for neuron in self.neurons:
            self.outputs.append(neuron.feed(inputs))
        if self.next == None:
            return self.outputs
        return self.next.feed(self.outputs)
        
    def propagate(self, expected = None):        
        for i in range(len(self.neurons)):
            if self.next == None:
                error = expected[i] - self.neurons[i].getOutput()
            else:
                error = self.next.getError(i)
            self.neurons[i].adjustDelta(error)
        if self.prev != None:
            self.prev.propagate()

    def getError(self, i):
        suma = 0
        for neuron in self.neurons:
            suma += neuron.getError(i)
        return suma

    def learn(self, inputs, learningRate):
        for neuron in self.neurons:
            neuron.learn(inputs, learningRate)
        if self.next != None:
            self.next.learn(self.outputs, learningRate)

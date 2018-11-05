from NN.NeuralNetwork import NeuralNetwork
from NN.NeuronLayer import NeuronLayer
from NN.Perceptron import Perceptron
from NN.Sigmoid import Sigmoid
import unittest

class TestPerceptron(unittest.TestCase):
    def test_feed(self):
        self.neuron = Perceptron(2, 2, [1, 1], 1)
        self.assertEqual(1, self.neuron.feed([2,2]))
        self.assertNotEqual(1, self.neuron.feed([0, -3]))

    def test_train(self):
        self.neuron = Perceptron(2, 2, [1, 1], 1)
        self.assertEqual(1, self.neuron.train([2,2], 0))
        self.assertNotEqual(self.neuron.bias, 2)
        self.assertNotEqual(self.neuron.weights, [1,1])

class TestSigmoid(unittest.TestCase):
    def setUp(self):
        self.neuron = Sigmoid(2, 2, [1, 1], 1)

    def test_feed(self): 
        self.assertAlmostEqual(1, self.neuron.feed([2,2]), delta=0.5)
        self.assertNotAlmostEqual(1, self.neuron.feed([0, -3]), delta=0.5)

    def test_train(self):
        neuron = Sigmoid(2, 2, [1, 1], 1)
        self.assertAlmostEqual(1, neuron.train([2,2], 0), delta=0.5)
        self.assertNotEqual(neuron.bias, 2)
        self.assertNotEqual(neuron.weights, [1,1])

    def test_getOutput(self):
        x = self.neuron.feed([2,2])
        self.assertEqual(x, self.neuron.getOutput())

    def test_getError(self):
        self.neuron.feed([-1,-1])
        self.neuron.adjustDelta(0.5)
        self.assertAlmostEqual(self.neuron.getError(0), 0.125, delta=0.01)

class TestNeuralNetwork(unittest.TestCase):
    def test_train(self):
        layer2 = NeuronLayer(1, 1, weights=[[0.3]], biases=[0.4])
        layer1 = NeuronLayer(1, 2, nextLayer=layer2, weights=[[0.4, 0.3]], biases=[0.5])
        layer2.setPreviousLayer(layer1)
        
        nn = NeuralNetwork([1],0)
        nn.setFirstLayer(layer1)
        nn.setOutputLayer(layer2)

        nn.train([1, 1], [1])

        n = layer1.neurons[0]
        self.assertAlmostEqual(0.502101508, n.bias)
        self.assertAlmostEqual(0.402101508, n.weights[0])
        self.assertAlmostEqual(0.302101508, n.weights[1])

        n = layer2.neurons[0]
        self.assertAlmostEqual(0.439377453, n.bias)
        self.assertAlmostEqual(0.330262548, n.weights[0])

if __name__ == "__main__":
    unittest.main()

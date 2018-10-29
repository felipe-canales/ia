import numpy as np
import matplotlib.pyplot as plt
import random
#from NN.Perceptron import Perceptron as Neuron
from NN.Sigmoid import Sigmoid as Neuron

def main():
    p = Neuron(2, learningRate = 0.1)

    inputs = [(0,0), (1,0), (0,1), (1,1)]
    expected = [0, 1, 1, 0]
    colors = []
    advancement = [0.0]
    for k in range(40):
        i = k % 4
        #plt.subplot(2, 1, 1)
        #plt.title("Puntos")
        #plt.plot(np.array([-50, 50]), np.array([-50, 50]))
        #plt.scatter(np.array([inputs[j][0] for j in range(i)]),\
        #            np.array([inputs[j][1] for j in range(i)]),\
        #            c = np.array(colors), cmap = 'coolwarm')

        #plt.subplot(2, 1, 2)
        plt.plot(np.array(range(k + 1)), np.array(advancement))
        plt.show()
        
        colors.append(p.train([inputs[i][0], inputs[i][1]], expected[i]))
        l = [1 if abs(colors[j] - expected[j]) < 0.5 else 0\
             for j in range(i + 1)]
        advancement.append(sum(l) / (k + 1.0))

main()

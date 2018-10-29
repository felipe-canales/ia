import numpy as np
import matplotlib.pyplot as plt
import random
import time
#from Perceptron import Perceptron as Neuron
from NN.Sigmoid import Sigmoid as Neuron


def main():
    p = Neuron(2, learningRate = 0.1)

    inputs = [(random.uniform(-50,50), random.uniform(-50,50))\
              for _ in range(200)]
    expected = [1 if inputs[i][1] < inputs[i][0] else 0 for i in range(200)]
    colors = []
    advancement = [0.0]
    for i in range(200):
        plt.subplot(2, 1, 1)
        plt.title("Puntos")
        plt.plot(np.array([-50, 50]), np.array([-50, 50]))
        plt.scatter(np.array([inputs[j][0] for j in range(i)]),\
                    np.array([inputs[j][1] for j in range(i)]),\
                    c = np.array(colors), cmap = 'coolwarm')

        plt.subplot(2, 1, 2)
        plt.plot(np.array(range(i + 1)), np.array(advancement))
        plt.show(block = False)
        time.sleep(3 - i/200.0)
        plt.close()

        colors.append(p.train([inputs[i][0], inputs[i][1]], expected[i]))
        #l = [1 if colors[j] > 0.5 and expected[j] == 1 or\
        #     colors[j] < 0.5 and expected[j] == 0 else 0\
        #     for j in range(i + 1)]
        l = [1 if abs(colors[j] - expected[j]) < 0.5 else 0\
             for j in range(i + 1)]
        advancement.append(sum(l) / (i + 1.0))

main()

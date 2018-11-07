import numpy as np
import matplotlib.pyplot as plt
import random
import time
from NN.Sigmoid import Sigmoid as Neuron


def main(trainer, inputs, expected, func,\
         epochs = 50, slow = False):
    p = trainer
    n = len(inputs)
    
    error = []
    advancement = [0.0]
    print("Training network")
    for i in range(epochs):
        print("Currently on epoch", i)
        results = []
        results = [p.train(inputs[j], expected[j]) for j in range(n)]
        advancement.append(sum(func(results, expected)) / len(results))
        error.append(trainer.getError())

        if slow:
            plt.plot(np.array(range(i + 2)), np.array(advancement))
            plt.show(block = False)
            time.sleep(3 - i/50.0)
            plt.close()
    if not slow:
        plt.plot(np.array(range(epochs + 1)), np.array(advancement))
        plt.xlabel("Epochs")
        plt.ylabel("Precision")
        plt.show()
    plt.plot(np.array(range(1,epochs + 1)), np.array(error))
    plt.ylabel("Error")
    plt.show()
    return p

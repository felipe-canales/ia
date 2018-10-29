import numpy as np
import matplotlib.pyplot as plt
import random

class Perceptron:
    def __init__(self, inputs, learningRate):
        self.w = [random.uniform(-2, 2) for _ in range(inputs)]
        self.bias = random.uniform(-2,2)
        self.lr = learningRate

    def feed(self, inputs, expected):
        n = len(inputs[0])
        results = []
        for i in range(n):
            if sum([self.w[j] * inputs[j][i] for j in range(len(self.w))]) + self.bias > 0:
                results.append(1)
            else:
                results.append(0)
        diff = sum(expected) - sum(results)
        
        if diff !=0:
            diff = sum([1 if expected[i] != results[i] else 0 for i in range(n)]) + diff/abs(diff)
        else:
            diff = sum([1 if expected[i] != results[i] else 0 for i in range(n)])
        self.w[0] += self.lr * diff * (sum(inputs[0]) / n)
        self.w[1] += self.lr * diff * (sum(inputs[1]) / n)
        self.bias += self.lr * diff
        print diff
        return results

    def getWeights(self):
        return self.w

    def getBias(self):
        return self.bias
    
def main():
    p = Perceptron(2, 0.01)
    
    objective = np.array([-50,50]), np.array([-50,50])
    inputs = [], []
    expected = []
    aprendizaje = [0]
    colors = []
    for _ in range(100):

        plt.subplot(2, 1, 1)
        plt.plot(objective[0], objective[1])
        plt.scatter(np.array(inputs[0]), np.array(inputs[1]), c=np.array(colors))
        plt.title('Puntos')

        plt.subplot(2, 1, 2)
        plt.plot(np.array(range(len(aprendizaje))), np.array(aprendizaje), 'o-')
        plt.xlabel('Iteraciones')
        plt.title('Curva de aprendizaje')

        plt.show()

        inputs = np.array([random.uniform(-50, 50) for i in range(200)]), \
                np.array([random.uniform(-50, 50) for i in range(200)])
        expected = [1 if inputs[1][i] < inputs[0][i] else 0 for i in range(200)]
        colors = p.feed(inputs, expected)
        aprendizaje.append(sum([1 if expected[i] == colors[i] else 0 for i in range(200)])/200.0)

main()
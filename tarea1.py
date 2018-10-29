import random
import learningTest
from NN.NeuralNetwork import NeuralNetwork

#inputs = []
data = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(2000)]
f = open("data.txt")
for i in range(2000):
    line = f.readline().split("  ")
    #inputs.append(list(map(lambda x: int(x) / 6, line))) # valores son enteros de 0 a 6
    data[i][int(i / 200)] = 1
    data[i].append(list(map(lambda x: int(x) / 6, line)))
random.shuffle(data)
inputs = [data[i].pop() for i in range(2000)]

red = NeuralNetwork([70, 50, 30, 10], 240)

def compare(list1, list2):
    final = []
    for i in range(len(list1)):
        val = 1
        for j in range(10):
            if abs(list1[i][j] - list2[i][j]) > 0.5:
                val = 0
                break
        final.append(val)
    return final

learningTest.main(red, inputs, data, compare, 25)

f.close()
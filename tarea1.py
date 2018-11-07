import random
import sys
import learningTest
from NN.NeuralNetwork import NeuralNetwork

layers = [[70, 10], \
          [70, 30 ,10], \
          [70, 50, 30, 10]]

setting = layers[0]
lrate = 0.5
if len(sys.argv) > 1:
    setting = layers[int(sys.argv[1]) - 1]
if len(sys.argv) > 2:
    lrate = float(sys.argv[2])

data = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(2000)]
f = open("data.txt")
for i in range(2000):
    line = f.readline().split("  ")
    data[i][int(i / 200)] = 1
    # valores son enteros de 0 a 6
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

learningTest.main(red, inputs, data, compare, epochs=15, lr=lrate)

f.close()
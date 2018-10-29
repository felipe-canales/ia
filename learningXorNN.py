import learningTest
from NN.NeuralNetwork import NeuralNetwork

red = NeuralNetwork([2, 2, 1], 2)
inputs = [(0,0), (1,0), (0,1), (1,1)]
expected = [[0], [1], [1], [0]]
def compare(list1, list2):
    final = []
    for i in range(len(list1)):
        if abs(list1[i][0] - list2[i][0]) < 0.5:
            final.append(1)
        else: final.append(0)
    return final

learningTest.main(red, inputs, expected, compare, 2000)

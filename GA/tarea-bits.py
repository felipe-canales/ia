from GeneticAlgorithm import GeneticAlgorithm
import sys

def main():
    # Parametros especificos
    if len(sys.argv) > 3:
        palabra = sys.argv[1]
        for char in palabra:
            if not char in "01":
                print("La palabra debe estar compuestas de 1s y 0s")
                exit()

        poblacion = int(sys.argv[2])
        nIter = int(sys.argv[3])
    # Parametros por defecto
    else:
        palabra "10100"
        poblacion = 20
        nIter = 100
    
    # Funcion de fitness
    f = lambda x,y: sum([1 for j in range(len(y)) if x[j] == y[j]])
    # GA
    ga = GeneticAlgorithm(len(palabra), poblacion, "01", palabra)
    # seed de random
    if len(sys.argv) > 4:
        if sys.argv[4] == 'r':
            ga.setSeed(None)
        else: 
            ga.setSeed(int(sys.argv[4]))

    ga.solve(f, f(palabra, palabra), nIter)



main()
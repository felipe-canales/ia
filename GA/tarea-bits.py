from GeneticAlgorithm import GeneticAlgorithm
import sys, random

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
        palabra = "10100"
        poblacion = 20
        nIter = 100
    
    # Funcion de fitness
    f = lambda x,y: sum([1 for j in range(len(y)) if x[j] == y[j]])
    # GA
    ga = GeneticAlgorithm(len(palabra), poblacion, "01", palabra)
    # seed de random
    if 'r' in sys.argv:
        random.seed(None)
    
    # imprimir cada generacion
    if 's' in sys.argv:
        ga.solve(f, f(palabra, palabra), nIter, verbose=False)
    else:
        ga.solve(f, f(palabra, palabra), nIter, verbose=True)

    y = ga.getProgress()
    r = ga.getRespuesta()
    rf = ""
    for char in r:
        rf += char

    print(" Palabra objetivo:\t", palabra, "fitness:", f(palabra, palabra),\
          "\n Palabra alcanzada:\t", rf, "fitness:", f(rf, palabra),\
          "\n Numero de generaciones:", len(y))



main()
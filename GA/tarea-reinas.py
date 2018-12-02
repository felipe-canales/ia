from GeneticAlgorithm import GeneticAlgorithm

import sys, random
import numpy as np
import matplotlib.pyplot as plt

# Funcion de fitness
def fitnessfunction(conf, void):
    errores = 0
    n = len(conf)
    for r1 in range(n):
        tieneError = False
        for r2 in range(n):
            if r1 == r2:
                continue
            if conf[r1] == conf[r2]: # estan en la misma posicion
                return 100
            if tieneError:
                continue
            c1 = (conf[r1]%n, int(conf[r1]/n)) #x,y de c1
            c2 = (conf[r2]%n, int(conf[r2]/n)) #x,y de c2
            # filas
            if c1[0] == c2[0]:
                errores += 1
                tieneError = True
                continue
            # columnas
            if c1[1] == c2[1]:
                errores += 1
                tieneError = True
                continue
            # diagonales \
            if (c1[0] - c1[1]) * (c2[0] - c2[1]) >= 0 \
                and conf[r1] % (n+1) == conf[r2] % (n+1):
                errores += 1
                tieneError = True
                continue
            # diagonales /
            if c1[0] + c1[1] == n - 1 and c2[0] + c2[1] == n - 1:
                errores += 1 # ambos en la diagonal principal
                tieneError = True
                continue
            if (c1[0] + c1[1] - n + 1) * (c2[0] + c2[1] - n + 1) > 0 \
                and conf[r1] % (n-1) == conf[r2] % (n-1):
                errores += 1
                tieneError = True
                continue
    return errores

def main():
    # Parametros especificos
    if len(sys.argv) > 3:
        tablero = int(sys.argv[1])
        poblacion = int(sys.argv[2])
        nIter = int(sys.argv[3])
    # Parametros por defecto
    else:
        tablero = 4
        poblacion = 50
        nIter = 50

    abc = [i for i in range(tablero**2)]
    # GA
    ga = GeneticAlgorithm(tablero, poblacion, abc)
    # seed de random
    if 'r' in sys.argv:
        random.seed(None)
    
    # imprimir cada generacion
    if 's' in sys.argv:
        ga.solve(fitnessfunction, 0, nIter, verbose=False, maximize=False)
    else:
        ga.solve(fitnessfunction, 0, nIter, verbose=True, maximize=False)

    p = ga.getProgress()
    r = ga.getRespuesta()
    rf = ""
    for y in range(tablero):
        rf += "-" + "---" * tablero + "\n|"
        for x in range(tablero):
            if x + y * tablero in r:
                rf += "Q |"
            else:
                rf += "  |"
        rf += "\n"
    rf += "-" + "---" * tablero  

    print(" Respuesta alcanzada:\n" + rf, "\nfitness:", fitnessfunction(r, None),\
          "\n Numero de generaciones:", len(p))

    print(r)

    plt.plot(np.array(range(len(p))), np.array(p))
    plt.xlabel("Generaciones")
    plt.ylabel("Mejor fitness")
    plt.show()

main()
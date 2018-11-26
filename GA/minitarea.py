from GeneticAlgorithm import GeneticAlgorithm

"""class BasicGeneticAlgorithm:
    def __init__(self, genes, population, solution = None):
        self.abc = "01"
        self.g = genes
        self.p = population
        self.population = [[self.abc[random.randint(0,1)] for _ in range(genes)]\
                            for __ in range(population)]
        self.solution = solution

    def solve(self, alternateCondition = False):
        f = []
        while((not 5 in f) or alternateCondition):
            f = self.checkFitness()
            mejor = f.index(max(f))
            print("Mejor de la generacion:", self.population[mejor], "fitness:", max(f))
            self.select(f)
            self.crossover()
            
        print("Solucion encontrada")
    
    def checkFitness(self):
        res = []
        for i in range(self.p):
            res.append(sum([1 for j in range(self.solution) if self.population[i][j] == self.solution[j]]))
        return res

    def select(self, fitness):
        promedio = sum(fitness)/self.p
        i = 0
        while i < len(fitness) and len(self.population) > (self.p / 2):
            if len(fitness) != len(self.population): print("Inconsistencia")
            if fitness[i] < promedio:
                fitness.pop(i)
                self.population.pop(i)
            else:
                i += 1

    def crossover(self):
        i = 0
        while len(self.population) < self.p:
            padres = [self.population[i*2], self.population[i*2 + 1]]
            self.population.append([padres[random.randint(0,1)][i] for i in range(self.g)])
            if len(self.population) >= self.p:
                break
            self.population.append([padres[random.randint(0,1)][i] for i in range(self.g)])
            i += 1"""
f = lambda x,y: sum([1 for j in range(len(y)) if x[j] == y[j]])

print("### Palabras con bits ###\n")
ins = ["010001001010010101", "10", "10100", "10101010", "11111"]
for i in range(5):
    print("--Caso", i + 1, ins[i])
    b = GeneticAlgorithm(len(ins[i]), 10, "01", ins[i])

    b.solve(f, len(ins[i]), iterations=10)
print("\n### Palabras con letras ###\n")
ins2 = ["ababa", "ccccc", "homestuck", "hello"]
for i in range(4):
    print("--Caso", i + 6, ins2[i])
    b = GeneticAlgorithm(len(ins2[i]), 20, "abcdefghijklmnopqrstuvwxyz", ins2[i])

    b.solve(f, len(ins2[i]), iterations=20)


print("### HOMESTUCK ###")
b = GeneticAlgorithm(len(ins2[2]), 200, "abcdefghijklmnopqrstuvwxyz", ins2[2])
b.solve(f, len(ins2[2]), iterations=2000000, mutation=1)
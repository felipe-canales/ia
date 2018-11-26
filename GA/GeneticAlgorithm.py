import random
random.seed(413)

class GeneticAlgorithm:
    def __init__(self, genes, population, abc, solution = None):
        self.abc = abc
        self.g = genes
        self.p = population
        self.population = [[self.abc[random.randint(0,len(abc)-1)] for _ in range(genes)]\
                            for __ in range(population)]
        self.solution = solution
        self.progress = []

    def solve(self, fitness, objective = None, iterations = 100, maximize = True, mutation=0):
        f = []
        i = 0
        mf = False
        while(mf != objective and i < iterations):
            f = self.checkFitness(fitness)
            mf = max(f)
            mejor = f.index(mf)
            print("Mejor de la generacion", i, ":", self.population[mejor], "fitness:", mf)
            self.progress.append(mf)
            self.select(f, maximize)
            self.crossover(mutation)
            random.shuffle(self.population)
            i += 1
    
    def checkFitness(self, foo):
        res = []
        for i in range(self.p):
            res.append(foo(self.population[i], self.solution))
        return res

    def select(self, fitness, maximize):
        promedio = sum(fitness)/self.p
        i = 0
        while i < len(fitness) and len(self.population) > (self.p / 2):
            if len(fitness) != len(self.population):
                raise RuntimeError("Inconsistencia")
            if fitness[i] < promedio and maximize:
                fitness.pop(i)
                self.population.pop(i)
            elif fitness[i] > promedio and not maximize:
                fitness.pop(i)
                self.population.pop(i)
            else:
                i += 1

    def crossover(self, mutationChance):
        i = 0
        l = len(self.abc) - 1
        while len(self.population) < self.p:
            padres = [self.population[i*2], self.population[i*2 + 1]]
            # First offspring
            new = [padres[random.randint(0,1)][i] for i in range(self.g)]
            if mutationChance == 0 or random.random() < mutationChance:
                new[random.randint(0, self.g - 1)] = self.abc[random.randint(0, l)]
            self.population.append(new)
            if len(self.population) >= self.p:
                break
            # Second offspring
            new = [padres[random.randint(0,1)][i] for i in range(self.g)]
            if mutationChance == 0 or random.random() < mutationChance:
                new[random.randint(0, self.g - 1)] = self.abc[random.randint(0, l)]
            self.population.append(new)
            i += 1
    
    def setSeed(self, x):
        random.seed(x)

    def getProgress(self):
        return self.progress
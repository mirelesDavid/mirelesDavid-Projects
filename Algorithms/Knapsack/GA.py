import random

class KnapsackItem:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

class GeneticKnapsack:
    def __init__(self):
        self.populationSize = 50
        self.genomeLength = 4
        self.mutationRate = 0.1
        self.crossoverRate = 0.7
        self.maxGenerations = 30
        self.tournamentSize = 2
        self.maxCapacity = 7
        
        self.items = [
            KnapsackItem(1, 1),
            KnapsackItem(3, 4),
            KnapsackItem(4, 5),
            KnapsackItem(5, 7)
        ]

    def calculateFitness(self, genome):
        totalValue = 0
        totalWeight = 0

        for idx, gene in enumerate(genome):
            if gene == 1:
                totalWeight += self.items[idx].weight
                totalValue += self.items[idx].value

        return 0 if totalWeight > self.maxCapacity else totalValue

    def generateInitialPopulation(self):
        return [[random.randint(0, 1) for _ in range(self.genomeLength)] 
                for _ in range(self.populationSize)]

    def selectParent(self, population):
        tournamentContenders = random.sample(population, self.tournamentSize)
        return max(tournamentContenders, key=self.calculateFitness)

    def performCrossover(self, parentA, parentB):
        if random.random() <= self.crossoverRate:
            crossoverPoint = random.randint(1, len(parentA) - 1)
            childA = parentA[:crossoverPoint] + parentB[crossoverPoint:]
            childB = parentB[:crossoverPoint] + parentA[crossoverPoint:]
            return childA, childB
        return parentA.copy(), parentB.copy()

    def performMutation(self, genome):
        return [1 - gene if random.random() < self.mutationRate else gene 
                for gene in genome]

    def getSolutionDetails(self, genome):
        selectedItems = []
        totalWeight = 0
        totalValue = 0

        for idx, gene in enumerate(genome):
            if gene == 1:
                selectedItems.append(idx + 1)
                totalWeight += self.items[idx].weight
                totalValue += self.items[idx].value

        return selectedItems, totalWeight, totalValue

    def solve(self):
        currentPopulation = self.generateInitialPopulation()
        bestGenome = None
        bestFitnessScore = 0
        stagnantGenerations = 0

        for generation in range(self.maxGenerations):
            nextGeneration = []

            while len(nextGeneration) < self.populationSize:
                parentA = self.selectParent(currentPopulation)
                parentB = self.selectParent(currentPopulation)

                offspringA, offspringB = self.performCrossover(parentA, parentB)
                offspringA = self.performMutation(offspringA)
                offspringB = self.performMutation(offspringB)

                nextGeneration.extend([offspringA, offspringB])

            nextGeneration = nextGeneration[:self.populationSize]
            currentPopulation = sorted(
                currentPopulation + nextGeneration,
                key=self.calculateFitness,
                reverse=True
            )[:self.populationSize]

            currentBestGenome = currentPopulation[0]
            currentFitnessScore = self.calculateFitness(currentBestGenome)

            if currentFitnessScore > bestFitnessScore:
                bestGenome = currentBestGenome
                bestFitnessScore = currentFitnessScore
                stagnantGenerations = 0
            else:
                stagnantGenerations += 1

            if (generation + 1) % 5 == 0:
                self.printGenerationReport(currentBestGenome, generation)

            if stagnantGenerations >= 10:
                print("\nEarly stopping: No improvement in last 10 generations")
                break

        self.printFinalReport(bestGenome)

    def printGenerationReport(self, genome, generation):
        selectedItems, totalWeight, totalValue = self.getSolutionDetails(genome)
        print(f"\nGeneration {generation + 1}")
        print(f"Best Value: {totalValue}")
        print(f"Total Weight: {totalWeight}/{self.maxCapacity}")
        print(f"Selected Items: {selectedItems}")

    def printFinalReport(self, genome):
        selectedItems, totalWeight, totalValue = self.getSolutionDetails(genome)
        print("\nBest Solution Found:")
        print(f"Total Value: {totalValue}")
        print(f"Total Weight: {totalWeight}/{self.maxCapacity}")
        print(f"Selected Items: {selectedItems}")
        print("\nSelected Items Details:")
        
        for itemIdx in selectedItems:
            item = self.items[itemIdx-1]
            print(f"Item {itemIdx}: Weight = {item.weight}, Value = {item.value}")
            
        print(f"\nSolution Chromosome: {genome}")

if __name__ == "__main__":
    solver = GeneticKnapsack()
    solver.solve()
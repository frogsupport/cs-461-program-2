from Activity import Activity
from Schedule import Schedule, randomSchedule
from Evolution import calculateAverageFitness, evolutionCycle, normalizedPopulation

mutationRate = 0.075 # Set the mutation rate

# Generate 500 random schedules
genesisPopulation = list()
for i in range(0, 501):
    genesisPopulation.append(randomSchedule())

# Calculate average fitness for population
previousGenerationAverageFitness = calculateAverageFitness(genesisPopulation)

# Compute the next generation
nextGeneration = evolutionCycle(genesisPopulation, mutationRate)

# Calculate this generations average fitness
nextGenerationAverageFitness = calculateAverageFitness(nextGeneration)

print("Generation 0 Average Fitness: " + str(previousGenerationAverageFitness))
print("Generation 1 Average Fitness: " + str(nextGenerationAverageFitness))

generationNum = 2

# Calculate the first 100 generations
for i in range(0, 100):
    previousGeneration = nextGeneration.copy()
    previousGenerationAverageFitness = nextGenerationAverageFitness

    nextGeneration = evolutionCycle(previousGeneration, mutationRate)
    nextGenerationAverageFitness = calculateAverageFitness(nextGeneration)

    print("Generation " + str(generationNum) + " Average Fitness: " + str(nextGenerationAverageFitness))

    generationNum += 1

# Repeat this process until there is no more than 1% improvement over the previous generation
while (((nextGenerationAverageFitness - previousGenerationAverageFitness) / previousGenerationAverageFitness) * 100) > 1.0:
    previousGeneration = nextGeneration.copy()
    previousGenerationAverageFitness = nextGenerationAverageFitness

    nextGeneration = evolutionCycle(previousGeneration, mutationRate)
    nextGenerationAverageFitness = calculateAverageFitness(nextGeneration)

    print("Generation " + str(generationNum) + " Average Fitness: " + str(nextGenerationAverageFitness))

    generationNum += 1

lastGeneration = normalizedPopulation(nextGeneration)

bestSchedule = lastGeneration[0]
bestSchedule.calculateFitness()

# Write the best schedule to a file
f = open("BestSchedule.txt", "w")
f.write(bestSchedule.writeSchedule())
f.close()
    



from scipy import special
import random

def sortByFitness(e):
    return e.fitnessScore

# Takes in a population of schedules. Computes the mating pools, reproduction of 
# the mating pools, mutation of the children, and returns the next generation.
def evolutionCycle(population):
    nextGeneration = list()

    # Get the fitness scores in an array
    fitnessScoreList = list()
    for individual in population:
        fitnessScoreList.append(individual.fitnessScore)

    # Normalize the fitness scores
    normalizedFitnessScores = special.softmax(fitnessScoreList)

    # Set the normalized fitness score for the schedule
    index = 0
    for individual in population:
        individual.setFitnessScore(normalizedFitnessScores[index])
        index += 1

    # Sort the population based on their fitness score
    population.sort(reverse=True, key=sortByFitness)

    # Get the top 10%
    populationIndex = 0
    top10MatingPool=list()
    while (populationIndex < (len(population) * 0.1)):
        top10MatingPool.append(population[populationIndex])
        populationIndex += 1

    # Get the top 30%
    populationIndex = 0
    top30MatingPool=list()
    while (populationIndex < (len(population) * 0.3)):
        top30MatingPool.append(population[populationIndex])
        populationIndex += 1

    # Get the top 50%
    populationIndex = 0
    top50MatingPool=list()
    while (populationIndex < (len(population) * 0.5)):
        top50MatingPool.append(population[populationIndex])
        populationIndex += 1

    # Reproduce the top 10%
    top10Length = len(top10MatingPool)
    for i in range(0, top10Length + 1):
        mummyIndex = random.randrange(0, top10Length)
        daddyIndex = random.randrange(0, top10Length)

        children = reproduce(top10MatingPool[mummyIndex], top10MatingPool[daddyIndex])

        nextGeneration.append(children)

    # Reproduce the top 30%

    # Reproduce the top 50%

    return nextGeneration

# Takes the mother and father, and returns two children
def reproduce(mummy, daddy, mutationRate):
    # Compute child 1

    # Optional mutation of child

    # Compute child 2

    # Optional mutation of child

    # Return both children

    return 0

# Mutates a child
def mutate(child):
    return 0

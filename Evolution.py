from scipy import special
from Schedule import Schedule
import random

def sortByFitness(e):
    return e.fitnessScore

# Takes in a population of schedules. Computes the mating pools, reproduction of 
# the mating pools, mutation of the children, and returns the next generation.
def evolutionCycle(population, mutationRate):
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

    # # Reproduce the top 50%
    # top50Length = int((len(population) * 0.2))
    # for i in range(0, top50Length + 1):
    #     mummyIndex = random.randrange(0, top50Length)
    #     daddyIndex = random.randrange(0, top50Length)

    #     children = reproduce(population[mummyIndex], population[daddyIndex], mutationRate)

    #     nextGeneration.append(children[0])
    #     nextGeneration.append(children[1])

    # Get the top 10%
    populationIndex = 0
    top10MatingPool=list()
    while (populationIndex < (len(population) * 0.1)):
        top10MatingPool.append(population[populationIndex])
        populationIndex += 1

    # Get the next 20%
    top30MatingPool=list()
    while (populationIndex < (len(population) * 0.3)):
        top30MatingPool.append(population[populationIndex])
        populationIndex += 1

    # Get the next 30%
    top50MatingPool=list()
    while (populationIndex < (len(population) * 0.5)):
        top50MatingPool.append(population[populationIndex])
        populationIndex += 1

    # Reproduce the top 10%
    top10Length = len(top10MatingPool)
    for i in range(0, top10Length + 1):
        mummyIndex = random.randrange(0, top10Length)
        daddyIndex = random.randrange(0, top10Length)

        children = reproduce(top10MatingPool[mummyIndex], top10MatingPool[daddyIndex], mutationRate)

        nextGeneration.append(children[0])
        nextGeneration.append(children[1])

    # Reproduce the top 30%
    top30Length = len(top30MatingPool)
    for i in range(0, top30Length + 1):
        mummyIndex = random.randrange(0, top30Length)
        daddyIndex = random.randrange(0, top30Length)

        children = reproduce(top30MatingPool[mummyIndex], top30MatingPool[daddyIndex], mutationRate)

        nextGeneration.append(children[0])
        nextGeneration.append(children[1])

    # Reproduce the top 50%
    top50Length = len(top50MatingPool)
    for i in range(0, top50Length + 1):
        mummyIndex = random.randrange(0, top50Length)
        daddyIndex = random.randrange(0, top50Length)

        children = reproduce(top50MatingPool[mummyIndex], top50MatingPool[daddyIndex], mutationRate)

        nextGeneration.append(children[0])
        nextGeneration.append(children[1])

    return nextGeneration

# Takes the mother and father, and returns two children
def reproduce(mummy, daddy, mutationRate):
    # Compute children
    child1 = mummy.crossover(daddy)
    child2 = daddy.crossover(mummy)

    # Optional mutation of children
    if (random.randint(0, 100) < (mutationRate * 100)):
        child1.mutate()
    if (random.randint(0, 100) < (mutationRate * 100)):
        child2.mutate()

    children = [child1, child2]

    return children

# Returns the average fitness of a population
def calculateAverageFitness(schedules):
    # Initialize the metrics
    averageFitness = 0.0
    scheduleCount = len(schedules)
    totalFitness = 0.0

    # Calculate the fitness of each schedule, calculate total fitness
    for schedule in schedules:
        schedule.calculateFitness()
        totalFitness += schedule.fitnessScore

    # Calculate average fitness for population
    averageFitness = (totalFitness / scheduleCount)

    return averageFitness
from Activity import Activity
from Schedule import Schedule, randomSchedule
from Evolution import evolutionCycle

# Generate 500 random schedules
genesisPopulation = list()
for i in range(0, 501):
    genesisPopulation.append(randomSchedule())

# Initialize the metrics for this population
averageFitness = 0.0
scheduleCount = 0.0
totalFitness = 0.0

# Calculate the fitness of each schedule, calculate total fitness
for schedule in genesisPopulation:
    schedule.calculateFitness()
    totalFitness += schedule.fitnessScore
    scheduleCount += 1

# Calculate average fitness for population
averageFitness = (totalFitness / scheduleCount)

# TODO: Evolution cycle function
nextGeneration = evolutionCycle(genesisPopulation)

# TODO: repeat this process until there is no more than 1% improvement over the previous generation
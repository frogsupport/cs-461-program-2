from Activity import Activity
from Schedule import Schedule, randomSchedule

# Generate 500 random schedules
genesisPopulation = list()
for i in range(0, 501):
    genesisPopulation.append(randomSchedule())

# Calculate the fitness of each schedule
for schedule in genesisPopulation:
    schedule.calculateFitness()

# print("Fitness: " + str(genesisPopulation[0].fitnessScore))

# TODO: Calculate the average fitness of the population

# TODO: naturalSelection Function: creates the mating pools. Maybe top 10%, next 20%, next 20%, remove bottom half

# TODO: reproduce function: input is two parents. returns two children

# TODO: crossover function that takes two schedules and returns their two children. used inside of reproduce

# TODO: mutate a certain amount of children. Will change a certain "gene" in an activity, or something.

# TODO: repeat this process until there is no more than 1% improvement over the previous generation
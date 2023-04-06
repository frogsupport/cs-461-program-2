from Activity import Activity
from Schedule import Schedule, randomSchedule

# TODO: Generate 500 random schedules
# Each random schedule will consist of random activities, so need a way of making random activities

genesisPopulation = list()
for i in range(0, 501):
    genesisPopulation.append(randomSchedule())

for schedule in genesisPopulation:
    print(schedule.SLA100A.fitnessScore)

# TODO: fitness function: calculate the fitness of a schedule

# TODO: Calculate the average fitness of the population

# TODO: naturalSelection Function: creates the mating pools. Maybe top 10%, next 20%, next 40%

# TODO: reproduce function: input is two parents. returns two children

# TODO: crossover function that takes two schedules and returns their two children. used inside of reproduce

# TODO: mutate a certain amount of children. Will change a certain "gene" in an activity, or something.

# TODO: repeat this process until there is no more than 1% improvement over the previous generation
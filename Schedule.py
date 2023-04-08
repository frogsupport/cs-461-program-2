import random
from Activity import Activity
from Room import Room, getRandomRoom

SLA100_PREFERRED_FACILITATORS = ["Glen", "Lock", "Banks", "Zeldin"]
SLA100_OTHER_FACILITATORS = ["Numen", "Richards"]

SLA191_PREFERRED_FACILITATORS = ["Glen", "Lock", "Banks", "Zeldin"]
SLA191_OTHER_FACILITATORS = ["Numen", "Richards"]

SLA201_PREFERRED_FACILITATORS = ["Glen", "Banks", "Zeldin", "Shaw"]
SLA201_OTHER_FACILITATORS = ["Numen", "Richards", "Singer"]

SLA291_PREFERRED_FACILITATORS = ["Lock", "Banks", "Zeldin", "Singer"]
SLA291_OTHER_FACILITATORS = ["Numen", "Richards", "Shaw", "Tyler"]

SLA303_PREFERRED_FACILITATORS = ["Glen", "Banks", "Zeldin"]
SLA303_OTHER_FACILITATORS = ["Numen", "Shaw", "Singer"]

SLA304_PREFERRED_FACILITATORS = ["Glen", "Banks", "Tyler"]
SLA304_OTHER_FACILITATORS = ["Numen", "Shaw", "Singer", "Richards", "Uther", "Zeldin"]

SLA394_PREFERRED_FACILITATORS = ["Tyler", "Singer"]
SLA394_OTHER_FACILITATORS = ["Richards", "Zeldin"]

SLA449_PREFERRED_FACILITATORS = ["Tyler", "Singer", "Shaw"]
SLA449_OTHER_FACILITATORS = ["Uther", "Zeldin"]

SLA451_PREFERRED_FACILITATORS = ["Tyler", "Singer", "Shaw"]
SLA451_OTHER_FACILITATORS = ["Uther", "Zeldin", "Richards", "Banks"]

COURSES = {"SLA100A": [50, SLA100_PREFERRED_FACILITATORS, SLA100_OTHER_FACILITATORS], 
           "SLA100B": [50, SLA100_PREFERRED_FACILITATORS, SLA100_OTHER_FACILITATORS], 
           "SLA191A": [50, SLA191_PREFERRED_FACILITATORS, SLA191_OTHER_FACILITATORS], 
           "SLA191B": [50, SLA191_PREFERRED_FACILITATORS, SLA191_OTHER_FACILITATORS], 
           "SLA201": [50, SLA201_PREFERRED_FACILITATORS, SLA201_OTHER_FACILITATORS],
           "SLA291": [50, SLA291_PREFERRED_FACILITATORS, SLA291_OTHER_FACILITATORS], 
           "SLA303": [60, SLA303_PREFERRED_FACILITATORS, SLA303_OTHER_FACILITATORS], 
           "SLA304": [25, SLA304_PREFERRED_FACILITATORS, SLA304_OTHER_FACILITATORS], 
           "SLA394": [20, SLA394_PREFERRED_FACILITATORS, SLA394_OTHER_FACILITATORS], 
           "SLA449": [60, SLA449_PREFERRED_FACILITATORS, SLA449_OTHER_FACILITATORS], 
           "SLA451": [100, SLA451_PREFERRED_FACILITATORS, SLA451_OTHER_FACILITATORS]}

TIME_SLOTS = [10, 11, 12, 13, 14, 15]

FACILITATORS = ["Lock", "Glen", "Banks", 
                "Richards", "Shaw", "Singer", 
                "Uther", "Tyler", "Numen", 
                "Zeldin"]

class Schedule:
    def __init__(self):
        self.Activities=list()
        self.fitnessScore=0.0

    def addActivity(self, activity):
        self.Activities.append(activity)

# Returns a random schedule
def randomSchedule():
    newRandomSchedule=Schedule()

    for course in COURSES:
        newRandomSchedule.addActivity(
            Activity(random.choice(TIME_SLOTS), 
                     getRandomRoom(), 
                     random.choice(FACILITATORS), 
                     COURSES[course][1], 
                     COURSES[course][2], 
                     COURSES[course][0], 
                     course))
        
    for activity in newRandomSchedule.Activities:
        print(activity.printActivity())
        print()
        print()

    return newRandomSchedule
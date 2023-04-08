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
        self.activities=list()
        self.fitnessScore=0.0

    def calculateFitness(self):
        # Calculate individual activity level fitness
        for activity in self.activities:
            activity.calculateFitness()
            self.fitnessScore += activity.fitnessScore

        # Activity is scheduled at same time in same room as another activity
        for activity in self.activities:
            activityRoom = activity.room
            activityTimeSlot = activity.timeSlot
            otherActivities = self.activities
            otherActivities.remove(activity)
            for otherActivity in otherActivities:
                otherRoom = otherActivity.room
                otherTimeSlot = otherActivity.timeSlot
                if (activityTimeSlot == otherTimeSlot) & (activityRoom == otherRoom):
                    self.fitnessScore -= 0.25

        # Check if facilitator is scheduled for more than one activity in a time slot
        for timeSlot in TIME_SLOTS:
            activeFacilitators = list()

            # Get the facilitators for the current time slot
            for activity in self.activities:
                if timeSlot == activity.timeSlot:
                    activeFacilitators.append(activity.facilitator)

            # Check for each facilitator how many times they are scheduled in this time slot
            for facilitator in FACILITATORS:
                numScheduledActivities = activeFacilitators.count(facilitator)
                if numScheduledActivities == 1:
                    self.fitnessScore += 0.2
                elif numScheduledActivities > 1:
                    self.fitnessScore -= 0.5
                
        # Check if facilitator is scheduled for more than 4 activities total
        

        # 2 sections of SLA101 and SLA 191 criteria

    def addActivity(self, activity):
        self.activities.append(activity)

    def printSchedule(self):
        print("Schedule:")
        print("-------------------------")
        for activity in self.activities:
            print(activity.printActivity())
            print()

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

    return newRandomSchedule
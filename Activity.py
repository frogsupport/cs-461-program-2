from Room import Room

class Activity:
    def __init__(
            self,
            timeSlot=int(),
            room=Room(),
            facilitator=str(),
            preferredFacilitators=list(),
            otherFacilitators=list(),
            expectedEnrollment=int(),
            courseNumber=str()):
        self.timeSlot=timeSlot
        self.room=room
        self.facilitator=facilitator
        self.preferredFacilitators=preferredFacilitators
        self.otherFacilitators=otherFacilitators
        self.expectedEnrollment=expectedEnrollment
        self.courseNumber=courseNumber
        self.fitnessScore=0.0

    def calculateFitness(self):
        # Room size
        if self.room.capacity < self.expectedEnrollment:
            self.fitnessScore -= 0.5
        elif self.room.capacity > (self.expectedEnrollment * 3):
            self.fitnessScore -= 0.2
        elif self.room.capacity > (self.expectedEnrollment * 6):
            self.fitnessScore -= 0.4
        else:
            self.fitnessScore += 0.3

        # Preferred facilitator status
        if self.facilitator in self.preferredFacilitators:
            self.fitnessScore += 0.5
        elif self.facilitator in self.otherFacilitators:
            self.fitnessScore =+ 0.2
        else:
            self.fitnessScore -= 0.1

    def printActivity(self):
        print("Course: " + self.courseNumber)
        print("Time Slot: " + str(self.timeSlot))

        self.room.printRoom()

        print("Facilitator: " + self.facilitator)
        print("Preferred Facilitators: ")

        for facilitator in self.preferredFacilitators:
            print(facilitator)

        print("Other Facilitators: ")

        for facilitator in self.otherFacilitators:
            print(facilitator)

        print("Expected Enrollment: " + str(self.expectedEnrollment))
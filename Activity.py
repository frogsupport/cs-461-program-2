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
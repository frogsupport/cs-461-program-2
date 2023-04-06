class Activity:
    def __init__(
            self,
            timeSlot=int(),
            room=str(),
            facilitator=str(),
            preferredFacilitators=list(),
            otherFacilitators=list(),
            expectedEnrollment=int(),
            courseNumber=str(),
            section=str()):
        self.timeSlot=timeSlot
        self.room=room
        self.facilitator=facilitator
        self.preferredFacilitators=preferredFacilitators
        self.otherFacilitators=otherFacilitators
        self.expectedEnrollment=expectedEnrollment
        self.courseNumber=courseNumber
        self.section=section
        self.fitnessScore=0.0

# Returns a randomely created activity
def randomActivity():
    return Activity()
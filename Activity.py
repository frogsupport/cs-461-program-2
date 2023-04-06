class Activity:
    def __init__(self):
        self.timeSlot=int()
        self.room=str()
        self.facilitator=str()
        self.preferredFacilitators=list()
        self.otherFacilitators=list()
        self.expectedEnrollment=list()
        self.courseNumber=list()
        self.section=list()
        self.fitnessScore=0.0

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
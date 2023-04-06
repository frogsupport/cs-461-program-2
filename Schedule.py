from Activity import Activity

class Schedule:
    def __init__(self):
        self.SLA100A=Activity()
        self.SLA100B=Activity()
        self.SLA191A=Activity()
        self.SLA191B=Activity()
        self.SLA201=Activity()
        self.SLA291=Activity()
        self.SLA303=Activity()
        self.SLA304=Activity()
        self.SLA394=Activity()
        self.SLA449=Activity()
        self.SLA451=Activity()
        self.fitnessScore=0.0

# Returns a random schedule
def randomSchedule():
    return Schedule()
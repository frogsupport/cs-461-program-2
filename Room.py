import random

class Room:
    def __init__(self, building=str(), roomNumber=str(), capacity=int()):
        self.building=building
        self.roomNumber=roomNumber
        self.capacity=capacity

    def printRoom(self):
        print("Building: " + self.building)
        print("Room Number: " + self.roomNumber)
        print("Capacity: " + str(self.capacity))

rooms= [Room("Slater", "003", 45), Room("Roman", "216", "30"), Room("Loft", "206", 75),
        Room("Roman", "201", 50), Room("Loft", "310", 108), Room("Beach", "201", 60),
        Room("Beach", "301", 75), Room("Logos", "325", 450), Room("Frank", "119", 60)]

def getRandomRoom():
    return random.choice(rooms)
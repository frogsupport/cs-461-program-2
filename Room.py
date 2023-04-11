import random

# A room for an activity
class Room:
    def __init__(self, building=str(), roomNumber=str(), capacity=int()):
        self.building=building
        self.roomNumber=roomNumber
        self.capacity=capacity

    # Prints an individual room
    def printRoom(self):
        print("Building: " + self.building)
        print("Room Number: " + self.roomNumber)
        print("Capacity: " + str(self.capacity))

    def writeRoom(self):
        room = str()

        room += "Building: " + self.building + "\n"
        room += "Room Number: " + self.roomNumber + "\n"
        room += "Capacity: " + str(self.capacity) + "\n"

        return room

# The valid rooms for an activity
rooms = [Room("Slater", "003", 45), Room("Roman", "216", 30), Room("Loft", "206", 75),
        Room("Roman", "201", 50), Room("Loft", "310", 108), Room("Beach", "201", 60),
        Room("Beach", "301", 75), Room("Logos", "325", 450), Room("Frank", "119", 60)]

# Returns a randomely selected room from the list of available rooms
def getRandomRoom():
    return random.choice(rooms)
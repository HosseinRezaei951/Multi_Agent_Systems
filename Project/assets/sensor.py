from .tools import euclidean_distance

class Sensor:
    def __init__(self, sensorNumber, sensorRadius, sensorPosition):
        self.number = sensorNumber
        self.status = -1 
        self.radius = sensorRadius
        self.position = sensorPosition
        self.conncectedGroup = []
        self.visibleTargets = []
        self.lockedTarget = None


    def print_sensorInfo(self):
        printString = "Sensor " + str(self.number) + ": \n"
        printString += "\tstatus: " + str(self.status) + "\n"
        printString += "\tradius: " + str(self.radius) + "\n"
        printString += "\tposition: " + str(self.position) + "\n"
        printString += "\tconncectedGroup: " + str([i+1 for i in self.conncectedGroup]) + "\n"
        printString += "\tvisibleTargets: " + str([j+1 for j in self.visibleTargets]) + "\n"
        if self.lockedTarget != None:
            printString += "\tlockedTarget: " + str(self.lockedTarget.number) + "\n"
        else:
            printString += "\tlockedTarget: " + str(self.lockedTarget) + "\n"
        print(printString)


    def update_status(self, newStatus = None):
        if newStatus != None:
            self.status = newStatus
        else:
            if self.visibleTargets:
                self.status = 0
            else:
                self.status = -1
    

    def trying_to_connect_to_other_sensor(self, newSensor):
        euclideanDistance = euclidean_distance(self.position, newSensor.position)
        if newSensor not in self.conncectedGroup and euclideanDistance <= self.radius :
            self.conncectedGroup.append(newSensor.number)
            print("\n>> sensor " + str(self.number) +
                  " connected to sensor " + str(newSensor.number))
            return True
        else:
            return False


    def trying_to_identify_visible_target(self, newVisibleTarget):
        euclideanDistance = euclidean_distance(self.position, newVisibleTarget.position)
        if newVisibleTarget not in self.visibleTargets and euclideanDistance <= self.radius :
            self.visibleTargets.append(newVisibleTarget)
            print("\n>> sensor " + str(self.number) +
                  " identified target " + str(newVisibleTarget.number))
            return True
        else:
            return False


    def lock_target(self, target):
        if self.lockedTarget == None:
            self.lockedTarget = target
            self.update_status(1)
            print("\n>> sensor " + str(self.number) +
                  " locked on target " + str(target.number))
            self.print_sensorInfo()
            return True
        else:
            return False
        

    def unlock_target(self, target):
        if self.lockedTarget != None:
            self.lockedTarget = None
            self.update_status()
            print("\n>> Sensor " + str(self.number) +
                  " unlocked on target " + str(target.number))
            self.print_sensorInfo()
            return True
        else:
            return False
        
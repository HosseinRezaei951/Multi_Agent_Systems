class Target:
    def __init__(self, TargetNumber, targetPosition):
        self.number = TargetNumber
        self.position = targetPosition
    
    def __repr__(self):
        return str(self.number) + str(self.position)
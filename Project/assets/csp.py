from math import trunc
from .sensor import Sensor
import numpy as np
from itertools import permutations

class CSP:
    def __init__(self, sensorsInfo):
        self.nSensors = 0
        self.nTargets = 0
        self.targets = []
        self.sensors = self.create_sensors(sensorsInfo)
        self.turningOn_all_sensors()
        
        
    def create_sensors(self, sensorsInfo):
        sensors = []
        self.nSensors = len(sensorsInfo)
        for i in range(self.nSensors):
            sensors.append(Sensor(sensorsInfo[i][0], sensorsInfo[i][1], sensorsInfo[i][2]))
 
        self.communicationMat = np.full((self.nSensors, self.nSensors), 0)
        return sensors


    def turningOn_all_sensors(self):
        for i in range(self.nSensors):
            for j in range(self.nSensors):
                if j != i:
                    self.sensors[i].trying_to_connect_to_other_sensor(self.sensors[j])
        self.update_communicationMat()
        

    def print_sensorsInfo(self):
        for i in range(self.nSensors):
            self.sensors[i].print_sensorInfo()


    def print_visibilityMat(self):
        t_len = len(str(self.nTargets)) + 1
        s_len = len(str(self.nSensors)) + 1
        
        printString = "\nVisibility Matrix:\n"

        firstSpaces = " " * (s_len)
        printString += " " + firstSpaces
        
        if self.nTargets != 0:
            for t in range(self.nTargets):
                tmp_printString = "t" + str(t+1)
                if len(tmp_printString) < t_len:
                    tmp_printString += " " * (abs(t_len-len(tmp_printString)))
                printString += " " + tmp_printString
            printString += "\n"

            for s in range(self.nSensors):
                for t in range(self.nTargets):
                    if t == 0:
                        tmp_printString = "S" + str(s+1)
                        if len(tmp_printString) < s_len:
                            tmp_printString += " " * (abs(s_len-len(tmp_printString)))
                        printString += " " + tmp_printString
                        
                    tmp_printString = str(self.visibilityMat[s,t])
                    if len(tmp_printString) < t_len:
                        tmp_printString += " " * (abs(t_len-len(tmp_printString)))
                    printString += " " + tmp_printString
                printString += "\n"
        else:
            printString += " no any target ... !\n"
        printString += "\n"
        print(printString)
    

    def print_communicationMat(self):
        s_len = len(str(self.nSensors)) + 1

        printString = "\nCommunication Matrix:\n"

        firstSpaces = " " * (s_len)
        printString += " " + firstSpaces
        
        for s in range(self.nSensors):
            tmp_printString = "S" + str(s+1)
            if len(tmp_printString) < s_len:
                 tmp_printString += " " * (abs(s_len-len(tmp_printString)))
            printString += " " + tmp_printString
        printString += "\n"
        
        for sx in range(self.nSensors):
            for sy in range(self.nSensors):
                if sy == 0:
                    tmp_printString = "S" + str(sx+1)
                    if len(tmp_printString) < s_len:
                        tmp_printString += " " * (abs(s_len-len(tmp_printString)))
                    printString += " " + tmp_printString
                    
                tmp_printString = str(self.communicationMat[sx,sy])
                if len(tmp_printString) < s_len:
                    tmp_printString += " " * (abs(s_len-len(tmp_printString)))
                printString += " " + tmp_printString
            printString += "\n"
        printString += "\n"
        print(printString)


    def update_visibilityMat(self):      
        for i in range(self.nSensors):
            for j in range(self.nTargets):
                if self.targets[j] in self.sensors[i].visibleTargets:
                    self.visibilityMat[i, j] = 0


    def update_communicationMat(self):
        connections = []
        for s in self.sensors:
            # Getting all permutations with lentgh 2 
            # of connections between sensors in one group
            comb = list(permutations(s.conncectedGroup, 2))
            connections.extend(comb)

        for conn in connections:
            self.communicationMat[conn[0]-1, conn[1]-1] = 1


    def add_newTarget(self, newTarget):
        if self.targets:
            if newTarget not in self.targets:
                self.nTargets += 1
                self.targets.append(newTarget)
                tmp_newTargetcolumn = np.full((self.nSensors, 1), -1)
                self.visibilityMat =  np.concatenate((self.visibilityMat, tmp_newTargetcolumn), axis=1)
                for s in self.sensors:
                    s.trying_to_identify_visible_target(newTarget)
                self.update_visibilityMat()
                return True
            else:
                return False
        else:
            self.nTargets += 1
            self.targets.append(newTarget)
            self.visibilityMat =  np.full((self.nSensors, 1), -1)
            for s in self.sensors:
                s.trying_to_identify_visible_target(newTarget)
            self.update_visibilityMat()
            return True
        

    def csp_run(self):
        for s in self.sensors:
            tmp_locked_targets = s.visibleTargets
            while tmp_locked_targets:
                locked_target = tmp_locked_targets.pop(0)
                if s.lock_target(locked_target) == True:
                    self.visibilityMat[s.number-1, locked_target.number-1] = 1
                                   
        
    

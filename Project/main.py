from assets.csp import CSP
from assets.target import Target

def main():
    
    '''
    sensors postition:
            S1  S2  S3
            S4  S5  S6
            S7  S8  S9
            S10 S11 S12
        
    each sensor info like that:
            [sensorNumber, sensorRadius, sensorPosition]
    '''
    sensors_radious = 1
    sensors_info = [
        [1, sensors_radious, (0, 0)],
        [2, sensors_radious, (0, 1)],
        [3, sensors_radious, (0, 2)],
        [4, sensors_radious, (1, 0)],
        [5, sensors_radious, (1, 1)],
        [6, sensors_radious, (1, 2)],
        [7, sensors_radious, (2, 0)],
        [8, sensors_radious, (2, 1)],
        [9, sensors_radious, (2, 2)],
        [10, sensors_radious, (3, 0)],
        [11, sensors_radious, (3, 1)],
        [12, sensors_radious, (3, 2)],
    ]

    
    targets_list = [
        Target(1, (1.5, 1)),
        Target(2, (2.5, 1))
    ]

    WST_CSP = CSP(sensors_info)
    WST_CSP.print_communicationMat()

    print("================== Start CSP Process ==================")
    while targets_list:
        tmp_target = targets_list.pop(0)
        WST_CSP.add_newTarget(tmp_target)
        WST_CSP.csp_run()
        WST_CSP.print_visibilityMat()

    input("================== End CSP Process ==================")

    
if __name__ == "__main__":
    main()
class MOTOR:

    def Prepare_To_Act():

        # pyrosim.Set_Motor_For_Joint(bodyIndex=robotId,
        #                             jointName="Torso_BackLeg",
        #                             controlMode=p.POSITION_CONTROL,
        #                             targetPosition=backTargetAngles[i],
        #                             maxForce=c.MAX_FORCE)


    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()


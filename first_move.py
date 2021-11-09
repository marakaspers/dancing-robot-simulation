import pybullet as p
import time
import pybullet_data
from math import sin, cos

physicsClient= p.connect(p.GUI)#or p.DIRECTfor non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
p.setGravity(0,0,-10)
planeId= p.loadURDF("plane.urdf")
robotStartPos= [0,0,1]
robotStartOrientation= p.getQuaternionFromEuler([0,0,0])
robotId= p.loadURDF("dumbo_color.urdf", robotStartPos, robotStartOrientation)
mode = p.POSITION_CONTROL
jointIndex= 0		# 2 motor leg thigh (1)
jointIndex1= 1		# 2 motor leg calf (1)
jointIndex2= 2		# 2 motor leg thigh (2)
jointIndex3= 3		# 2 motor leg calf (2)
jointIndex4= 4		# 1 motor leg calf (1)
jointIndex5= 5		# 1 motor leg calf (2)
jointIndex6= 6		# 1 motor leg calf (3)
jointIndex7= 7		# 1 motor leg calf (4)

# original test parameters
# w = 0.01	# beat parameter chould increase/decrease with 1% based on picked up beat
# a = 0.4		
# b = 0.8
# c = 0.6

# # our first walking parameters
# w = 0.02		# 2/100 	# beat parameter chould increase/decrease with 1% based on picked up beat
# a = 0.5		# 120/240	
# b = 0.2		# 50/240
# c = 0		# 0/240

w = 0.2	# beat parameter chould increase/decrease with 1% based on picked up beat
a = 0
b = 1
c = 0 # change phase
# other continuous functions

for i in range (10000):
	p.stepSimulation()

	p.setJointMotorControl2(robotId, jointIndex, controlMode=mode, targetPosition=(a+b*sin(i*w+c))) 	# 2 motor leg thigh (1)
	# p.setJointMotorControl2(robotId, jointIndex, controlMode=mode, targetPosition=0.4+0.8*sin(i*0.01+0.6))
	p.setJointMotorControl2(robotId, jointIndex1, controlMode=mode, targetPosition=(a+b*sin(i*w+c)))	# 2 motor leg calf (1)
	p.setJointMotorControl2(robotId, jointIndex2, controlMode=mode, targetPosition=(a+b*cos(i*w+c)))	# 2 motor leg thigh (2)
	p.setJointMotorControl2(robotId, jointIndex3, controlMode=mode, targetPosition=(a+b*cos(i*w+c)))	# 2 motor leg calf (2)
	p.setJointMotorControl2(robotId, jointIndex4, controlMode=mode, targetPosition=(a+b*sin(i*w+c)))	# 1 motor leg calf (1)
	p.setJointMotorControl2(robotId, jointIndex5, controlMode=mode, targetPosition=(a+b*sin(i*w+c)))	# 1 motor leg calf (2)
	p.setJointMotorControl2(robotId, jointIndex6, controlMode=mode, targetPosition=(a+b*cos(i*w+c)))	# 1 motor leg calf (3)
	p.setJointMotorControl2(robotId, jointIndex7, controlMode=mode, targetPosition=(a+b*cos(i*w+c)))	# 1 motor leg calf (4)

	time.sleep(1./240.) # make this dependent on song
	# change dance speed with the beat
	time.sleep(w)
robotPos, robotOrn= p.getBasePositionAndOrientation(robotId)
print(robotPos, robotOrn)
p.disconnect()


# print(p.getNumJoints(robotId))
import os
import pybullet_data
import pybullet as p
import time
import pyrosim.pyrosim as pyrosim
import numpy as np

if not os.path.exists("data"):
    os.makedirs("data")

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-119.8)
planeId = p.loadURDF("plane.urdf")

robotId = p.loadURDF("robot.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

# Create a numpy vector filled with zeros
backLegSensorValues = np.zeros(1000)


# Iterate 1000 times and step the simulation in each iteration
for i in range(1000):
    # Print the loop variable
    print("Loop variable:", i)
    
    # Step the simulation
    p.stepSimulation()

    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Leg")

    # Introduce a delay of 1/60th of a second
    time.sleep(1/60)


    print("Initial backLegSensorValues:", backLegSensorValues)  # Print the initial values

# Save backLegSensorValues to a file in the "data" directory
np.save("data/my_sensor_values.npy", backLegSensorValues)

p.disconnect()

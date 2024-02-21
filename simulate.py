import pybullet_data
import pybullet as p
import time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")

p.loadSDF("boxes.sdf")

# Iterate 1000 times and step the simulation in each iteration
for i in range(1000):
    # Print the loop variable
    print("Loop variable:", i)
    
    # Step the simulation
    p.stepSimulation()

    # Introduce a delay of 1/60th of a second
    time.sleep(1/60)

p.disconnect()

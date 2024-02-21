import pybullet as p
import time

physicsClient = p.connect(p.GUI)

p.loadSDF("box.sdf")

# Iterate 1000 times and step the simulation in each iteration
for i in range(1000):
    # Print the loop variable
    print("Loop variable:", i)
    
    # Step the simulation
    p.stepSimulation()

    # Introduce a delay of 1/60th of a second
    time.sleep(1/60)

p.disconnect()

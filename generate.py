import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

pyrosim.Start_SDF("boxes.sdf")

# Initial parameters
num_blocks = 10
initial_size = 1.0
num_towers = 5

# Loop to create towers
for i in range(num_towers):
    for j in range(num_towers):
        for k in range(num_blocks):
            # Update position for each block
            x = i   # Adjust the spacing between towers (e.g., 2 units)
            y = j   # Adjust the spacing between blocks in a row (e.g., 2 units)
            z = k * initial_size  # Each block sits directly on the one below it

            # Update size for each block (90% of the size of the block below it)
            length *= 0.9
            width *= 0.9
            height *= 0.9

            # Send Cube statement
            pyrosim.Send_Cube(name=f"Box{i}_{j}_{k}", pos=[x, y, z], size=[length, width, height])

        # Reset initial size for each tower
        length = 1.0
        width = 1.0
        height = 1.0

pyrosim.End()


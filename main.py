import matplotlib.pyplot as plt
import numpy as np

# Generating random 4D data
num_points = 100
x = np.random.rand(num_points)
y = np.random.rand(num_points)
z = np.random.rand(num_points)
color_dimension = np.random.rand(num_points)  # Fourth dimension represented by color
size_dimension = np.random.rand(num_points) * 100  # Random size for points

# Creating a 4D scatter plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot with color representing the fourth dimension
scatter = ax.scatter(x, y, z, c=color_dimension, s=size_dimension, cmap='plasma', alpha=0.7)

# Adding color bar
cbar = plt.colorbar(scatter)
cbar.set_label('Fourth Dimension')

# Labels
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

plt.title('4D Scatter Plot')

plt.show()

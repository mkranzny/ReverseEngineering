import numpy as np
from stl import mesh
from tetgen import TetGen
from mpl_toolkits import mplot3d
from matplotlib import pyplot
import pyvista as pv

# stl_mesh = mesh.Mesh.from_file("SocketScrew.stl")
# stl_mesh = mesh.Mesh.from_file("bolt.stl")
stl_mesh = mesh.Mesh.from_file("link.stl")
vertices = stl_mesh.vectors.reshape(-1, 3) 
faces = np.arange(len(vertices)).reshape(-1, 3)
print(vertices)
print(faces)

tet = TetGen(vertices, faces)
tetra_mesh = tet.tetrahedralize(order=1)
grid = tet.grid
grid.plot(show_edges=True)

print(tetra_mesh)

# get cell centroids
cells = grid.cells.reshape(-1, 5)[:, 1:]
cell_center = grid.points[cells].mean(1)

# extract cells below the 0 xy plane
mask = cell_center[:, 2] < 0
cell_ind = mask.nonzero()[0]
subgrid = grid.extract_cells(cell_ind)

# advanced plotting
plotter = pv.Plotter()
plotter.add_mesh(subgrid, 'lightgrey', lighting=True, show_edges=True)
# plotter.add_mesh(sphere, 'r', 'wireframe')
plotter.add_legend([[' Input Mesh ', 'r'],
                    [' Tessellated Mesh ', 'black']])
plotter.show()

# pv.plot(tetra_mesh)

# tetra_mesh.plot(show_edges=True)

# tetra_points = tetra_mesh.points 
# tetra_elements = tetra_mesh.elements

print("Tetrahedral Mesh Generated!")

# # Create a new plot
# figure = pyplot.figure()
# print("here1")

# axes = mplot3d.Axes3D(figure)
# print("here2")


# # Load the STL files and add the vectors to the plot
# your_mesh = mesh.Mesh.from_file('coax.stl')
# print("here3")

# axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))
# print("here4")


# # Auto scale to the mesh size
# # scale = your_mesh.points.flatten()
# print("here5")

# # axes.auto_scale_xyz(scale, scale, scale)
# print("here6")
# print(your_mesh)

# # Show the plot to the screen
# pyplot.show()



try:
    while True:
        n = 1
        # time.sleep(1)

except KeyboardInterrupt:
    print("here3")
    print("Exiting Program")

except Exception as exception_error:
    print("Error occurred. Exiting Program")
    print("Error: " + str(exception_error))

finally:
    pass




# To create a tetrahedral mesh from an STL file in Python, you can use libraries like meshio, PyVista, or TetGen. Here's an example workflow:

# 1. Using TetGen with numpy-stl
# This approach uses numpy-stl to read the STL file and TetGen to generate the tetrahedral mesh.


# Copy code
# import numpy as np
# from stl import mesh
# from tetgen import TetGen
# Load STL file
# stl_mesh = mesh.Mesh.from_file("your_model.stl")

# Extract vertices and faces
# vertices = stl_mesh.vectors.reshape(-1, 3) faces = np.arange(len(vertices)).reshape(-1, 3)

# Initialize TetGen
# tet = TetGen(vertices, faces)

# Generate tetrahedral mesh
# tetra_mesh = tet.tetrahedralize(order=1)

# Access tetrahedral mesh data
# tetra_points = tetra_mesh.points tetra_elements = tetra_mesh.elements

# print("Tetrahedral Mesh Generated!")


# Copy code
# 2. Using PyVista for Visualization
# PyVista can help visualize the STL and tetrahedral mesh.


# Copy code
# import pyvista as pv
# Load STL file
# stl_mesh = pv.read("your_model.stl")

# Convert to tetrahedral mesh
# tetra_mesh = stl_mesh.tetrahedralize()

# Visualize
# tetra_mesh.plot(show_edges=True)


# Copy code
# 3. Using meshio for File Conversion
# If you want to convert an STL file to a tetrahedral mesh format (e.g., .msh), you can use meshio.


# Copy code
# import meshio
# Read STL file
# mesh = meshio.read("your_model.stl")

# Write to a tetrahedral mesh format
# meshio.write("your_model.msh", mesh)


# Copy code
# These methods allow you to generate and manipulate tetrahedral meshes from STL files. Choose the one that best fits your needs!
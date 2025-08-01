# https://pypi.org/project/meshio/
# https://polyfem.github.io/polyfempy_doc/

import numpy as np
from stl import mesh
from tetgen import TetGen
import polyfempy as pf
import trimesh
import meshio
import pyvista as pv
import matplotlib.pyplot as plt
import time

# # this section works
# stl_mesh = mesh.Mesh.from_file("link.stl")
# vertices = stl_mesh.vectors.reshape(-1, 3) 
# faces = np.arange(len(vertices)).reshape(-1, 3)
# tet = TetGen(vertices, faces)
# nodes, elem = tet.tetrahedralize(order=1)
# grid = tet.grid
# grid.plot(show_edges=True)
# print(nodes, elem)
# grid.save("link.vtk")
# pv.save_meshio("link.mesh", grid)

# # this works
# mesh = meshio.read("link.vtk")
# # mesh.write("link.obj", file_format="obj")
# mesh.write("link.msh", file_format="gmsh")
# # mesh.write("link.msh", file_format="gmsh22")
# # mesh.write("link.ply", file_format="ply")


mesh_path = "link.mesh"
# mesh_path = "plate_hole.obj"
settings = pf.Settings(
    discr_order=1,
    pde=pf.PDEs.LinearElasticity
)
settings.set_material_params("E", 210000)
settings.set_material_params("nu", 0.3)
problem = pf.Problem()
# problem.set_x_symmetric(1)
# problem.set_y_symmetric(4)
problem.set_displacement(1, [0, 0, 0], is_dim_fixed=None)
problem.set_force(3, [100, 0, 0])
settings.problem = problem
solver = pf.Solver()
print("here1")
solver.settings(settings)
print("here2")
solver.load_mesh_from_path(mesh_path, normalize_mesh=True)
time.sleep(10)
# solver.load_mesh_from_path(mesh_path)
print("here3")
solver.solve()
time.sleep(30)
print("here4")
solver.export_vtu("out.vtu")
pts, tets, disp = solver.get_sampled_solution()
vertices = pts + disp
mises, _ = solver.get_sampled_mises_avg()
# print(vertices)
# x1 = vertices[:, 0] 
# y1 = vertices[:, 1]
# z1 = vertices[:, 2]
# x2 = pts[:, 0] 
# y2 = pts[:, 1]
# z2 = pts[:, 2]
# print(x1)
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# ax.scatter(x1, y1, z1, color='blue')
# ax.scatter(x2, y2, z2, color='red')
# plt.show()
# while True:
#     n = 1

#solve might run on a separate thread...need a good way to wait on it

try:
    while True:
        # n = 1
        time.sleep(1)

except KeyboardInterrupt:
    # pts, tets, disp = solver.get_sampled_solution()
    # vertices = pts + disp
    # mises, _ = solver.get_sampled_mises_avg()
    # print(vertices)
    # x1 = vertices[:, 0] 
    # y1 = vertices[:, 1]
    # z1 = vertices[:, 1]
    # x2 = pts[:, 0] 
    # y2 = pts[:, 1]
    # z2 = pts[:, 1]
    # plt.scatter(x1, y1, color='blue', label='Points')
    # plt.scatter(x2, y2, color='red', label='Points')
    # plt.show()
    print("hereEnd")
    print("Exiting Program")
    
except Exception as exception_error:
    print("Error occurred. Exiting Program")
    print("Error: " + str(exception_error))

finally:
    pass

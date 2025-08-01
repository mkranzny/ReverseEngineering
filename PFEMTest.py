# https://polyfem.github.io/python_examples/
# conda install conda-forge::polyfempy

import numpy as np
import polyfempy as pf
import time
import matplotlib.pyplot as plt

def create_quad_mesh(n_pts):
    extend = np.linspace(0,1,n_pts)
    x, y = np.meshgrid(extend, extend, sparse=False, indexing='xy')
    pts = np.column_stack((x.ravel(), y.ravel()))
    
    faces = np.ndarray([(n_pts-1)**2, 4],dtype=np.int32)

    index = 0
    for i in range(n_pts-1):
        for j in range(n_pts-1):
            faces[index, :] = np.array([
                j + i * n_pts,
                j+1 + i * n_pts,
                j+1 + (i+1) * n_pts,
                j + (i+1) * n_pts
            ])
            index = index + 1
            
    return pts, faces

mesh_path = "plate_hole.obj"

settings = pf.Settings(
    discr_order=1,
    pde=pf.PDEs.LinearElasticity
)

settings.set_material_params("E", 210000)
settings.set_material_params("nu", 0.3)

problem = pf.Problem()

problem.set_x_symmetric(1)

problem.set_y_symmetric(4)

problem.set_force(3, [100, 0])

settings.problem = problem

solver = pf.Solver()
print("here1")
solver.settings(settings)
solver.load_mesh_from_path(mesh_path, normalize_mesh=True)

solver.solve()

#solve might run on a separate thread...need a good way to wait on it

try:
    while True:
        n = 1
        # time.sleep(1)

except KeyboardInterrupt:
    pts, tets, disp = solver.get_sampled_solution()
    vertices = pts + disp
    mises, _ = solver.get_sampled_mises_avg()
    print(vertices)
    x1 = vertices[:, 0] 
    y1 = vertices[:, 1]
    x2 = pts[:, 0] 
    y2 = pts[:, 1]
    plt.scatter(x1, y1, color='blue', label='Points')
    plt.scatter(x2, y2, color='red', label='Points')
    plt.show()
    print("here3")
    print("Exiting Program")

except Exception as exception_error:
    print("Error occurred. Exiting Program")
    print("Error: " + str(exception_error))

finally:
    pass


# print("here2")
# print(solver)
# pts, tets, disp = solver.get_sampled_solution()
# print("here3")
# vertices = pts + disp

# mises, _ = solver.get_sampled_mises_avg()


# print(vertices)
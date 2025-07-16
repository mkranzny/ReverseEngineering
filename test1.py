import numpy as np
import trimesh
from trimesh.transformations import scale_matrix, translation_matrix

# attach to logger so trimesh messages will be printed to console
trimesh.util.attach_to_log()

# mesh objects can be loaded from a file name or from a buffer
# you can pass any of the kwargs for the `Trimesh` constructor
# to `trimesh.load`, including `process=False` if you would like
# to preserve the original loaded data without merging vertices
# STL files will be a soup of disconnected triangles without
# merging vertices however and will not register as watertight
mesh1 = trimesh.load('link.stl')
mesh2 = trimesh.load('serpentine.stl')

# preview mesh in an opengl window if you installed pyglet and scipy with pip
#mesh1.show()
#mesh2.show()

#translate = translation_matrix(list(map(lambda x: -(x[0] + x[1]) / 2.0, mesh1.bounds)))
# temp = [[1,0,0,1],[0,1,0,1],[0,0,1,1]],[0,0,0,1]
# temp2 = np.array(temp)
translate = translation_matrix([1,1,1])
#print(translate)
mesh1.apply_translation([10,0,10])

meshunion = trimesh.boolean.union([mesh1, mesh2])
meshunion.show()

meshdiff = trimesh.boolean.difference([mesh1, mesh2])
meshdiff.show()
print(mesh1)
print(mesh1.vertices)
print(mesh1.faces)
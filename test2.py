import numpy as np
import cv2 as cv
import trimesh

mesh1 = trimesh.load('Bolt.stl')
print(trimesh.bounds.oriented_bounds(mesh1))
# slice = mesh1.section(plane_origin=mesh1.centroid, plane_normal=[0, 1, 0])
# slice.show()
mesh1.show()

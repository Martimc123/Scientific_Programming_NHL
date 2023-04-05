import numpy as np
import copy

def swap(coords: np.ndarray):
    coords[0:,[0,1]], coords[0:,[2,3]] = coords[0:,[1,0]], coords[0:,[3,2]]
    return coords

""" | 1 - Can you spot the obvious error?
    | Ans: the obvious error is that on index 1 we are assgining the value of itself instead of the correct value of index 0.
    |
    | 2 - After fixing the obvious error it is still wrong, how can this be fixed?
    | Ans: Even if we fix this, it's still wrong because for each line it's assigning the value of y to x instead of swapping them, for example x1=y1, and since objects in python are passed by
    | reference, whenever we do the reverse assignment of y to x, the value is already changed hence why its only copies the value of y to x.
    |   To fix this what we must do is slice through each line of the matrix and instead of returning the index we want to switch, we need to return a list with the pair of indices we want want
    | to switch, in order to guarantee that we dont change the values themselves, since they're passed by reference, but instead based on a list containing those values, so that we can do the reverse assignment as well and avoid using a direct reference.
    |   In the code itself, what we must do is replace this line " coords[:, 0], coords[:, 1], coords[:, 2], coords[:, 3], = coords[:, 1], coords[:, 1], coords[:, 3], coords[:, 2] " with " coords[0:,[0,1]], coords[0:,[2,3]] = coords[0:,[1,0]], coords[0:,[3,2]] "
    | and we will get the correct output
"""

coords = np.array([[10, 5, 15, 6, 0],
                [11, 3, 13, 6, 0],
                [5, 3, 13, 6, 1],
                [4, 4, 13, 6, 1],
                [6, 5, 13, 16, 1]])
coords_copy = copy.deepcopy(coords)
swapped_coords = swap(coords)
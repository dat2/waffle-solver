
import random
import itertools
import numpy as np

ROTATION_MATRICES = {
    str([1, 0, 0]) + 'clockwise': np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]]),
    str([1, 0, 0]) + 'counterclockwise': np.array([[-1, 0, 0], [0, 0, 1], [0, -1, 0]]),
    str([-1, 0, 0]) + 'clockwise': np.array([[-1, 0, 0], [0, 0, 1], [0, -1, 0]]),
    str([-1, 0, 0]) + 'counterclockwise': np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]]),
    str([0, 1, 0]) + 'clockwise': np.array([[0, 0, -1], [0, 1, 0], [1, 0, 0]]),
    str([0, 1, 0]) + 'counterclockwise': np.array([[0, 0, 1], [0, -1, 0], [-1, 0, 0]]),
    str([0, -1, 0]) + 'clockwise': np.array([[0, 0, 1], [0, -1, 0], [-1, 0, 0]]),
    str([0, -1, 0]) + 'counterclockwise': np.array([[0, 0, -1], [0, 1, 0], [1, 0, 0]]),
    str([0, 0, 1]) + 'clockwise': np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]]),
    str([0, 0, 1]) + 'counterclockwise': np.array([[0, -1, 0], [1, 0, 0], [0, 0, -1]]),
    str([0, 0, -1]) + 'clockwise': np.array([[0, -1, 0], [1, 0, 0], [0, 0, -1]]),
    str([0, 0, -1]) + 'counterclockwise': np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])
}
class Piece:
    def __init__(self, position, color, type):
        self.type = type
        self.color = color
        self.position = position

    def __str__(self):
        return str([self.position, self.color])

    def __repr__(self):
        return str([self.position, self.color])

def listFromVec(vec):
    dis = []
    for elem in list(set(itertools.permutations(vec))):
        dis.append(list(elem))
    return dis

class Cube:
    def __init__(self):
        self.pieces = []
        self.colors = ['r', 'g', 'y', 'o', 'b', 'w']
        self.vectors = { 'r': [1,0,0], 'g': [0,1,0], 'b': [0, -1, 0], 'y': [0, 0, 1], 'o': [-1,0,0], 'w': [0,0,-1] }
        self.middles = listFromVec([1,0,0]) + listFromVec([-1,0,0])
        self.corners = listFromVec([1,1,1]) + listFromVec([-1,-1,-1]) + listFromVec([-1,-1,1]) + listFromVec([1,1,-1])
        self.edges = listFromVec([1,1,0]) + listFromVec([-1,-1,0]) + listFromVec([1,-1,0])
        self.edges_colors = ['rg', 'gy', 'ry', 'ow', 'bw', 'ob', 'og', 'rw', 'yb', 'rb', 'yo', 'gw']
        self.corner_colors = ['gyr', 'wob', 'oyb', 'rbw', 'wog', 'rgw', 'ybr', 'goy']
        self.faces = {'r': [], 'g': [], 'b': [], 'w': [], 'y': [], 'o': []}

    def randomInit(self):
        for col, pos in zip(self.colors, self.middles):
            self.pieces.append(Piece(pos, col, 'middle'))

        for col, edge in zip(self.edges_colors, self.edges):
            self.pieces.append(Piece(edge, col, 'edge'))

        for col, corner in zip(self.corner_colors, self.corners):
            self.pieces.append(Piece(corner, col, 'corner'))

        for piece1 in self.pieces:
            if piece1.type == 'middle':
                cols = piece1.color
                self.faces[cols] = [piece1]
                for piece2 in self.pieces :
                    if piece2.type != 'middle':
                        index_of_one = np.nonzero(piece1.position)[0][0]
                        if piece2.position[index_of_one] == piece1.position[index_of_one]:
                            self.faces[cols].append(piece2)

    def getColoursForFace(self, color):
        return self.faces[color]

    def rotateForColor(self, color, clockwise=True):
        translation = None
        for piece in self.faces[color]:
            if piece.type == 'middle':
                translation = piece.position

        matrix = ROTATION_MATRICES[str(translation) + 'clockwise'] if clockwise else ROTATION_MATRICES[str(translation) + 'counterclockwise']
        for piece in self.faces[color]:
            # print(piece)
            piece.position = list(matrix.dot(piece.position))
            print(piece)


cube = Cube()
cube.randomInit()
cube.rotateForColor('r')
# for piece in cube.getFaceForColor('r'):
#     print(piece)
# for piece in cube.pieces:
#     print(piece)


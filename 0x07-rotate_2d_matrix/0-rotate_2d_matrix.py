#!/usr/bin/python3
""" 2D matrix transformation """


def rotate_2d_matrix(matrix):
    """
        This module rotates a n X n 2D matrix 90 degree clockwise

        Args:
            matrix (list): Matrix to be rotated
    """

    rotatedMatrix = []
    count = 0

    for row in range(len(matrix)):
        newRow = []
        for col in reversed(matrix):
            newRow.append(col[count])
        count += 1
        rotatedMatrix.append(newRow)
    
    return rotatedMatrix
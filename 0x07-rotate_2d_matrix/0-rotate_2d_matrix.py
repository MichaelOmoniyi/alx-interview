#!/usr/bin/python3
""" 2D matrix transformation """


def rotate_2d_matrix(matrix):
    """
        This module rotates a n X n 2D matrix 90 degree clockwise

        Args:
            matrix (list): Matrix to be rotated
    """

    rotatedMatrix = []

    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

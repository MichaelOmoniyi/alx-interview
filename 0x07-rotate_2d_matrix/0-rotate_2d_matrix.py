#!/usr/bin/python3
""" 2D matrix transformation """


def rotate_2d_matrix(matrix):
    """
        This module rotates a n X n 2D matrix 90 degree clockwise

        Args:
            matrix (list): Matrix to be rotated
    """

    rotatedMatrix = []

    for row in range(len(matrix)):
        for col in range(row+1, len(matrix)):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    for row in matrix:
        row.reverse()
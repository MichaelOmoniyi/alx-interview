#!/usr/bin/python3
"""
    Island Perimeter
"""


def island_perimeter(grid):
    """
        Calculates the perimeter of the island described in grid

        Args:
            grid (list): a list of list of integers

        Return:
            perimeter of the island described in grid
    """

    rlen = len(grid)
    clen = len(grid[0])
    perimeter = 0

    for row in range(rlen):
        for col in range(clen):
            if grid[row][col] == 1:
                if row == 0:
                    perimeter += 1
                if row == (rlen - 1):
                    perimeter += 1
                if col == 0:
                    perimeter += 1
                if col == (clen - 1):
                    perimeter += 1
                if row > 0 and grid[row - 1][col] == 0:
                    perimeter += 1
                if row < (rlen - 1) and grid[row + 1][col] == 0:
                    perimeter += 1
                if col > 0 and grid[row][col - 1] == 0:
                    perimeter += 1
                if col < (clen - 1) and grid[row][col + 1] == 0:
                    perimeter += 1

    return perimeter

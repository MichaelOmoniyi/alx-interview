#!/usr/bin/python3
"""
Contains the function that checks if the boxes in a box can be unlocked or not
"""


def checkbox(boxes, keys, index, checked):
    """
        This function checks if the box can be unlocked
        Args:
            box (list): The box to be checked
            keys (list): A list of keys available to unlock the box
        Return:
            True, if box can be unlocked otherwise False
    """

    for box in range(1, len(boxes)):
        if box in checked:
            continue
        else:
            if index in keys:
                return [True, box]
            elif boxes[box]:
                for key in boxes[box]:
                    if key in keys:
                        return [True, box]
    return [False, box]


def canUnlockAll(boxes):
    """
        This function checks if all the boxes can be unlocked
            Args:
                boxes (list): A list of boxes to be checked
            Return:
                True, if all boxes can be unlocked otherwise false
    """

    keys = []
    unlocked = [0]

    for key in boxes[0]:
        keys.append(key)

    for box in range(1, len(boxes)):
        unlock = checkbox(boxes, keys, box, unlocked)
        if unlock[0] is True:
            for key in boxes[box]:
                keys.append(key)
            unlocked.append(unlock[1])

    if len(unlocked) == len(boxes):
        return True
    else:
        return False

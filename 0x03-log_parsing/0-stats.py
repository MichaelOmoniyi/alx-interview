#!/usr/bin/python3
import sys


def printStats(stat_dicts, file_size):
    """
    This module prints the stats.
    Args:
        stat_dicts (dict): A dictionary containging the status codes
        file_size (integer): The total file size calculated
    Returns:
        Nothing
    """

    print("File size: {}".format(file_size))
    for key, val in sorted(stat_dicts.items()):
        if val != 0:
            print("{}: {}".format(key, val))


totalFileSize = 0
statusCode = 0
counter = 0
stat_dicts = {"200": 0,
              "301": 0,
              "400": 0,
              "401": 0,
              "403": 0,
              "404": 0,
              "405": 0,
              "500": 0}

try:
    for line in sys.stdin:
        parsedLine = line.split()
        parsedLine = parsedLine[::-1]

        if len(parsedLine) > 2:
            counter += 1

            if counter <= 10:
                totalFileSize += int(parsedLine[0])
                statusCode = parsedLine[1]

                if (statusCode in stat_dicts.keys()):
                    stat_dicts[statusCode] += 1

            if counter == 10:
                printStats(stat_dicts, totalFileSize)
                counter = 0

finally:
    printStats(stat_dicts, totalFileSize)

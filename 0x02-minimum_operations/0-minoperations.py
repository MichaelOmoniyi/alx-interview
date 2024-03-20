#!/usr/bin/python3
"""In this project I devised a soltion to solve the minimum operation challenge"""


def checkIfPrimeNumber(num):
    """"
        This fuction calculates checks if num is a prime number
        Args:
            num (integer): The number to be checked
        Return:
            False and an integer if number is not a prime number otherwise True
    """
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return [False, i]
    return [True, num]

def operations(num):
    """
        This function calculates the number of operations required using prime factorization
        Args:
            num (interger): The number of characters to be gotten
        Return:
            The minimum amount of operations
    """

    operation = 0
    divisor = checkIfPrimeNumber(num)
    if divisor[0]:
        return divisor[1]
    else:
        operation += divisor[1]
        currentNum = num // divisor[1]
        return operation + operations(currentNum)
    
def minOperations(n):
    """
        This function calculates the fewest number of opeartion needed to result in n H characters in the file
        Args:
            n (integer): The number of characters
        Return:
            The number of operations, otherwise 0
    """

    if n <= 0:
        return 0
    elif checkIfPrimeNumber(n):
        return n
    else:
        return operations(n)
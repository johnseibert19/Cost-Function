# -*- coding: utf-8 -*-
"""
Finds the cost of an integer using a set of sub-algorithms built into a list
found in the driver algorithm.

@author: John Seibert
"""
from math import sqrt, ceil, log

costs = [1, 1, ]
operands = [1, 1, ]
number = int(input("Enter any number: "))

for j in range(number + 1):
    if j > 1:
        costs.append(j)
        operands.append(j)

def multiply(x):
    """
    Checks two operands to see if they multiply to x. If so, the cost is the
    sum of the cost of operand 1 and the cost of operand 2.
    
    Parameters
    ----------
    x : int
        Current value used in the driver algorithm.

    Returns
    -------
    min : int
        The minimum cost obtained using solely multiplication.
    operands : str
        Displays the factors obtained from multiplication.
    """
    factors = []
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            factors.append(i)
    min = x
    operands = x
    for i in range(len(factors)):
        if costs[factors[i]] + costs[factors[len(factors) - 1 - i]] + 3 < min:
            min = costs[factors[i]] + costs[factors[len(factors) - 1 - i]] + 3
            operands = f'{factors[i]}*{factors[len(factors) - 1 - i]}'
    return min, operands

def fibonacci(x):
    """
    Checks to see if the number passed from the driver algorithm is the sum of 
    the last two numbers in the sequence. If so, the cost of the given number
    is the cost(n) + 4 (where n is the nth Fibonacci number). 
    Parameters
    ----------
    x : int
        Current value used in the driver algorithm.

    Returns
    -------
    min : int
        Returns the minimum cost obtained using solely the Fibonacci sequence. 
        if x is in the Fibonacci sequence. Else, it returns the number
        obtained from the driver algorithm, essentially doing nothing.
    operands : str
        Displays the nth Fibonacci number.
    """
    fib = [1, 1, ]
    for i in range(2, number + 1):
        if i == fib[len(fib) - 1] + fib[len(fib) - 2]:
            fib.append(i)
    if x > 1 and x in fib:   
        return costs[fib.index(x)] + 4, f'F({fib.index(x)})'
    else:
        return x, x

def successor(x):
    """
    Determines if the cost of the current number, x, is no more than 1 + C(x-1). 
    If not, we determine the above equation as the cost. 
    
    Parameters
    ----------
    x : int
        Current value used in the driver algorithm.

    Returns
    -------
    min : int
        Returns the minimum cost obtained using solely the successor. If it is
        the new minimum, we display the new number. 
    operands : str
        Displays the explanation of the cost as S(x-1).
    """
    return costs[x-1] + 1, f'S({x-1})'

def add(x):
    """
    Iterates through two operands, i and x - i, and sees if 
    C(i) + C(x - i) + 3 is less than the minimum cost previously assigned.
    
    Parameters
    ----------
    x : int
        Current value used in the driver algorithm.

    Returns
    -------
    min : int
        The cost of x attained through solely addition. Should it be less than
        the minimum attained through every other method, it becomes C(x).
    operands : str
        An explanation using the two addends found for x, should it be the
        new minimum cost.

    """
    min = x
    operands = x
    for i in range(1, x // 2 + 1):
        if costs[i] + costs[x - i] + 2 < min:
            min = costs[i] + costs[x - i] + 2
            operands = f'{i}+{x-i}'
    return min, operands

def exponent(x):
    """
    Iterates through two operands, b and e, and b^e = x, we see if 
    C(b) + C(e) + 4 is less than the minimum. If so, the cost of x
    becomes the new minimum.

    Parameters
    ----------
    x : int
        The current number passed through the driver program.

    Returns
    -------
    min : int
        The cost of x using just exponentiation, and if the above equation is
        less than the minimum this becomes C(x).
    operands : str
        A showing of the base and power that lead to the new cost, should that
        be necessary.
    """
    powers = []
    for base in range(2, ceil(sqrt(x)) + 1):
        for expo in range(2, int(log(x, base)) + 2):
            power = base ** expo
            if power == x:
                    powers.append(base)
                    powers.append(expo)
    min = x
    operands = x
    for i in range(0, len(powers), 2):
        if costs[powers[i]] + costs[powers[i + 1]] + 4 < min:
            min = costs[powers[i]] + costs[powers[i + 1]] + 4
            operands = f'{powers[i]}^{powers[i + 1]}'
    return min, operands

def binary(x):
    """
    Converts an integer passed through the driver algorithm into its binary
    representation. We take the length of the binary representation and give
    a complexity charge of 7 to find the cost using solely binary.
    
    Parameters
    ----------
    x : int
        Current value passed through the driver algorithm.

    Returns
    -------
    min : int
        The cost of x using solely binary. If this is the new minimum cost, the
        output, C(x) becomes the minimum.
    operands : str
        The binary representation is the operands, should the minimum cost be
        attributed to the binary representation.
    """
    binary = bin(x)
    bin_rep = binary[2:]
    cost = len(bin_rep) + 7
    return cost, bin_rep
    
function_list = [fibonacci, successor, add, exponent, binary, multiply]

for j in range(1, number + 1):
    min = costs[j]
    op = operands[j]
    for f in function_list:
            y, c = f(j)
            if y < min:
                min = y
                culp = c
            costs[j] = min
            operands[j] = op
            
for a in range(0, len(costs)):
    print(a, costs[a], operands[a])
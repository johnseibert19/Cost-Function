from math import sqrt, ceil, log

costs = [1, 1]
culprits = [1, 1]
u_bounds = [1, 1]

number = int(input("Enter any number: "))

def multiply(x):
    factors = []
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            factors.append(i)

    min_cost = x
    culprit = x
    for i in range(len(factors)):
        if costs[factors[i]] + costs[factors[len(factors) - 1 - i]] + 3 < min_cost:
            min_cost = costs[factors[i]] + costs[factors[len(factors) - 1 - i]] + 3
            culprit = f"{factors[i]}*{factors[len(factors) - 1 - i]}"

    return min_cost, culprit


def fibonacci(x):
    fib = [1, 1]
    for i in range(2, number + 1):
        if i == fib[len(fib) - 1] + fib[len(fib) - 2]:
            fib.append(i)

    if x > 1 and x in fib:
        return costs[fib.index(x)] + 4, f"F({fib.index(x)})"
    else:
        return x, x


def successor(x):
    return costs[x - 1] + 1, f"S({x - 1})"


def add(x):
    min_cost = x
    culprit = x
    for i in range(1, x // 2 + 1):
        if costs[i] + costs[x - i] + 2 < min_cost:
            min_cost = costs[i] + costs[x - i] + 2
            culprit = f"{i}+{x - i}"

    return min_cost, culprit


def exponent(x):
    powers = []
    for base in range(2, ceil(sqrt(x)) + 1):
        for expo in range(2, int(log(x, base)) + 2):
            power = base**expo
            if power == x:
                powers.append(base)
                powers.append(expo)

    min_cost = x
    culprit = x
    for i in range(0, len(powers), 2):
        if costs[powers[i]] + costs[powers[i + 1]] + 4 < min_cost:
            min_cost = costs[powers[i]] + costs[powers[i + 1]] + 4
            culprit = f"{powers[i]}^{powers[i + 1]}"

    return min_cost, culprit


def binary(x):
    return len(bin(x)[2:]) + 7, bin(x)[2:]


def main():
    for j in range(2, number + 1):
        costs.append(j)
        culprits.append(j)
        u_bounds.append(len(bin(j)[2:]) + 7)

    function_list = [fibonacci, successor, add, exponent, multiply, binary]
    for j in range(1, number + 1):
        min_cost = costs[j]
        culprit = culprits[j]
        for f in function_list:
            y, c = f(j)
            if y < min_cost:
                min_cost = y
                culprit = c

        costs[j] = min_cost
        culprits[j] = culprit

        print(j, costs[j], culprits[j])


if __name__ == "__main__":
    main()

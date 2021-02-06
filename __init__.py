from math import factorial
def zeta(num, MAX): #MAX is accuracy and this calculates ζ(num)
    factors, P = [0 for i in range(MAX)], []
    for i in range(2, MAX):
        q = 100 * i / MAX
        if int(q) == q: print(f'{int(q)}%')
        if i == MAX - 1: print('100%')
        if (factorial(i - 1) + 1) % i: # If not prime
            for p in P:
                i2, c = i, 0
                while not i2 % p: c, i2 = c + 1, i2 // p
                factors[i] = max(c, factors[i])
        else:
            P += [i]
            factors[i] = 1
    return MAX / (sum([factors.count(i) for i in range(num)]))
print(zeta(3, 10000)) # To print out ζ(3) with low accuracy

# mathmatical algorithm // elementary number theory

import math

# Sieve of Eratosthenes
def Eratosthenes(N):
    Max = int(N ** 0.5) + 1
    PrimeBool = [True] * (N + 9)

    for i in range(2, Max):
        if PrimeBool[i] == True:
            for j in range(i*2, N+1, i):
                PrimeBool[j] = False

    return PrimeBool

# a^b mod m
def Power_mod(a, b, m):
    p = 1
    q = a % m
    Max = math.ceil(math.log2(b))
    for i in range(Max):
        if (b >> i) & 1 == 1:
            p = (p * q) % m
        
        q = (q * q) % m

    return p
# Manacher's algorithm
N, Q = [int(e) for e in input().split()]
S2 = input()

S = S2[0]
for i in range(1, N):
    S = S + "#" + S2[i]


L = len(S)
c, r = 0, 0
R = [0] * L
while c < L:
    while (c - r >= 0) and (c + r < L):
        if S[c-r] == S[c+r]:
            r += 1
        else:
            break
    
    R[c] = r

    d = 1
    while c - d >= 0:
        if d + R[c-d] < r:
            R[c+d] = R[c-d]
            d += 1
        else:
            break
    
    c += d
    r -= d


Pal_odd = [0] * N
Pal_even = [0] * (N-1)
for j in range(L):
    if j % 2 == 0:
        i = j // 2
        Pal_odd[i] = (R[j] + 1) // 2
    elif j % 2 == 1:
        i = j // 2
        Pal_even[i] = R[j] // 2


for q in range(Q):
    X, Y = [int(e) for e in input().split()]
    Z = Y - X
    Center = (X + Y) // 2 - 1
    if Z % 2 == 0:
        if (Z // 2 + 1) <= Pal_odd[Center]:
            print("Yes")
        else:
            print("No")
    
    elif Z % 2 == 1:
        if (Z + 1) // 2 <= Pal_even[Center]:
            print("Yes")
        else:
            print("No")
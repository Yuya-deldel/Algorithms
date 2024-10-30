# Z algorithm
# Z[i]: length of longest common prefix between S and S[i...N-1]

S = input()
L = len(S)

Z = [L] * L
i, j = 1, 0
while i < L:
    while i + j < L:
        if S[j] == S[i+j]:
            j += 1
        else:
            break
    
    Z[i] = j

    if j == 0:
        i += 1
        continue

    k = 1
    while k < j:
        if k + Z[k] < j:
            Z[i+k] = Z[k]
            k += 1
        else:
            break
    i += k
    j -= k

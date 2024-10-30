### Rolling Hash mod 2^61-1
# high speed / hash collision resistant
# inspired by @keymoon 
###################################################
#remark: 2^61-1 is a Mersenne prime and ~ 2.3*10^18
#remark: a*2^61 = a (mod 2^61-1)

import random

def division_bit(a,n):          # a = p*2^n + q
    p = a >> n                  # p = a // 2^n
    q = a & ((1 << n) - 1)      # q = a and 111...1 ("1" * n)
    return [p, q]

# a*b mod 2^61-1 without overflow
def multiplication(a, b):       # a*b = (ap*2^31 + aq) * (bp*2^31 + bq)
    A = division_bit(a, 31)     #     = ap*bp * 2^62 + (ap*bq + aq*bp) * 2^31 + aq*bq
    ap, aq = A[0], A[1]         #     = 2*ap*bp + Cp + Cq * 2^31 + aq*bq
    B = division_bit(b, 31)     # C = ap*bq + aq*bp ; C = Cp * 2^30 + Cq 
    bp, bq = B[0], B[1]
    C = division_bit(ap*bq + aq*bp, 30)
    cp, cq = C[0], C[1]
    return modMersenne(2*ap*bp + cp + cq*(1 << 31) + aq*bq)

def modMersenne(x):
    m_prime = (1 << 61) - 1     # 2^61-1
    y = x
    while y < 0:
        y += m_prime
    
    D = division_bit(y, 61)
    d = D[0] + D[1]             # d = dp*2^61 + dq = dp + dq
    if d >= m_prime:
        d -= m_prime
    
    return d
    
##############################################################
# define conversion function: Char => Int
def Char_to_Int(s):
    return ord(s) - ord('a') + 1
    
# Hash calculation: return hash(s[l ~ r])
def Hash(S, Base, l, r):          
    N = len(S)
    H = [0] * (N + 1)
    B = [1] * (N + 1)
    for i in range(1, N+1):
        H[i] = multiplication(H[i-1], Base) + Char_to_Int(S[i-1])
        B[i] = multiplication(B[i-1], Base)
    
    return modMersenne(H[r] - multiplication(H[l-1], B[r-l+1]))

# Matching
N, Q = [int(e) for e in input().split()]
S = input()
Base = random.randrange(27, 50)
H = [0] * (N + 1)
B = [1] * (N + 1)
for i in range(1, N+1):
    H[i] = multiplication(H[i-1], Base) + Char_to_Int(S[i-1])
    B[i] = multiplication(B[i-1], Base)

for k in range(Q):
    l1, r1, l2, r2 = [int(e) for e in input().split()]
    h1 = modMersenne(H[r1]  - multiplication(H[l1 - 1], B[r1 - l1 + 1]))
    h2 = modMersenne(H[r2]  - multiplication(H[l2 - 1], B[r2 - l2 + 1]))
    if h1 == h2:
        print("Yes")
    else:
        print("No")

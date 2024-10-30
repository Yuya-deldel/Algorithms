# Manacher's algorithm
# How long are maximal radius of palindrome for all i in [0, L-1]?
# *palindrome: level, civic, noon, refer ect...
# example
# a b a a a b a b a
# 1 2 1 4 1 2 3 2 1

S = input()
L = len(S)

# M_pal : set of maximal radius // (c, r) = (center, radius)
# Lemma: For all (c, r), (c-d, rl), (c+d, rr) in M_pal,
#        (1), (2) or (3) is True:
#        (1): rl < r - d  =>  rr = rl
#        (2): rl = r - d  =>  rr >= r - d
#        (3): rl > r - d  =>  rr = r - d
#
#             r     c     r
#        <---------- ----------> :S 
# (1)       <--->       <--->               // this follows from (2)
# (2)    <------>      <--------->          // if not, it contradicts to maximality of (c+d, rr)
# (3)  <--------->        <---->            // if rr > r - d, it contradicts to maximality of (c, r)

# if (1)       : R(c+d) = rr         // by induction, R(c+d) is uniquely determined
# if (2) or (3): R(c+d) >= r - d     

# for odd-length palindrome
c, r = 0, 0                                 
R = [0] * L
while (c < L):
    while (c - r >= 0) and (c + r < L):     
        if S[c-r] == S[c+r]:                # calculating R[c]
            r += 1                          
        else:
            break

    R[c] = r
    
    d = 1
    while c - d >= 0:
        if d + R[c-d] < r:                  # in case of (1)
            R[c+d] = R[c-d]                 # R[c+d] is uniquely determined by induction
            d += 1
        else:
            break

    print(c,r,d)

    c += d
    r -= d                                  # if not (1), then (2) or (3) : R(c+d) >= r - d

# to extend this method to even-length palindrome, substitute S=abc.. into S'=a*b*c*...

print(R)
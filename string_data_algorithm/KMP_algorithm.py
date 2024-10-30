# KMP algorithm
# How many are S[0,i-1]'s prefix/suffix characters coinside?
# example: 
# i : 0 1 2 3 4 5 6 7 8
# S : a a b a a b a a a      (* A[i] < |S[0,i-1]|)
# A : _ 0 1 0 1 2 3 4 5 2

S = input()
N = len(S)

# Morris-Pratt algorithm: A[i] = MP[i]

# <      S       >   |    <--------> = S[0, MP[i]-1]    (because len(<-------->) = MP[i])
#      <-------->a   |    if a=b :  j += 1  
# <-------->b        |    elif a!=b :
#                    |        check c such that
#           <--->a   |        <---> = S[0, MP[MP[i]-1]]    (because len(<--->) = MP[MP[i]-1])
#      <--->b        |        if a=c : j = MP[j], j += 1
# <--->c             |        elif a!=c :  ... repeat.

MP = [] * (N+1)                             
MP[0] = -1                            
j = -1                                
for i in range(0, N):                 
    while (j >= 0) and (S[i] != S[j]):
        j = MP[j]                     
                                      
    j += 1                            
    MP[i+1] = j


# repeat number of times: ~ O(1) (average) // ~ O(N) (worst) : worst example: S = aa...aab
#   => total average amount of calculation ~ O(N)

# How to reduce repeat number of times?

# Knuth-Morris-Pratt algorithm: A[i] = KMP[i]

KMP = [] * (N+1)                             
KMP[0] = -1                            
j = -1                                
for i in range(0, N):                 
    while (j >= 0) and (S[i] != S[j]):
        j = KMP[j]                     
                                      
    j += 1

    if S[i+1] == S[j]:
        KMP[i+1] = KMP[j]                   # if S[KMP[j]] != S[j] and S[i+1] = S[j]
    else:                                   # then obviously S[i+1] != S[KMP[j]]
        KMP[i+1] = j                        # => in next step, j = KMP[j]

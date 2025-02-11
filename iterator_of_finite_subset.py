# iterator of finite subset
# 
# A: finite set, B: A's subset
# (N_A, N_B) => iterator array
#
# (8, 3) => [[0, 1, 2], [0, 1, 3], ... , [5, 6, 7]]

def iterator_of_finite_subset(n, n_sub):
    if (n_sub == 0) | (n < n_sub):
        raise ValueError("invalid arguments")

    x = (1 << n_sub) - 1
    Iter = []

    while (x < (1 << n)) :
        Iter.append(bits_to_array(x, n))

        minimum_right_bit = x & (-x)
        left_bits = x + minimum_right_bit
        right_aligned_bits = ((left_bits ^ x) >> 2) // minimum_right_bit
        x = left_bits | right_aligned_bits
    
    return Iter

def bits_to_array(x, n):
    array = []

    for i in range(0, n):
        if ((x & (1 << i)) != 0):
            array.append(i)
    
    return array

# x:                  xxx0 1111 0000
# minimum_right_bit:  0000 0001 0000
# left_bits:          xxx1 0000 0000
# left_bits ^ x:      0001 1111 0000
# right_aligned_bits: 0000 0000 0111
# new_x:              xxx1 0000 0111

# x and new_x have same number of '1' bits

##############################################
# test code
#print(iterator_of_finite_subset(10, 1))
#print(bits_to_array(7, 4))
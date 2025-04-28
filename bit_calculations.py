# bit calculations

# rounding down to 2^n
# 0101 1000 => 0100 0000
def rounding_down_bits(x):
    x = x | (x >> 1)
    x = x | (x >> 2)
    x = x | (x >> 4)
    x = x | (x >> 8)
    x = x | (x >> 16)
    x = x | (x >> 32)       # 0111 1111
    return x - (x >> 1)     # 0111 1111 - 0011 1111

# rounding up to 2^n
# 0101 1000 => 1000 0000
def rounding_up_bits(x):
    x -= 1
    x = x | (x >> 1)
    x = x | (x >> 2)
    x = x | (x >> 4)
    x = x | (x >> 8)
    x = x | (x >> 16)
    x = x | (x >> 32)       # 0111 1111
    return x + 1            # 1000 0000

# counting number of '1' bits
# 10100111 => 5(0000 0101)
def population_count(x):
    x -= ((x >> 1) & 0x5555555555555555)                            # x = (x & 0x55...5) + ((x >> 1) & 0x55...5) 
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0F0F0F0F0F0F0F0F                         # x = (x & 0x0F0F...0F) + ((x >> 4) & 0x0F0F...0F)
    x += x >> 8
    x += x >> 16
    x += x >> 32
    return x & 0x7F

# when average number of '1' bits <= 4
def population_count_small_case(x):
    count = 0
    while x != 0:
        count += 1
        x = x & (x - 1)     # leftmost '1' bit off
    
    return count

# parity of bits (number of bits is odd or even)
def parity(x):
    y = x ^ (x >> 1)
    y = y ^ (y >> 2)
    y = y ^ (y >> 4)
    y = y ^ (y >> 8)
    y = y ^ (y >> 16)
    y = y ^ (y >> 32)
    return y & 1    # rightmost bit

# number of leading '0's in 64bit machine
# for large number of '0's
def number_of_leading_zeros(x):
    count = 64
    y = x >> 32
    if y != 0:
        count -= 32
        x = y
    y = x >> 16
    if y != 0:
        count -= 16
        x = y
    y = x >> 8
    if y != 0:
        count -= 8
        x = y
    y = x >> 4
    if y != 0:
        count -= 4
        x = y
    y = x >> 2
    if y != 0:
        count -= 2
        x = y
    if (x >> 1) == 0:
        return count - x
    else:
        return count - 2
    
# for small number of '0's
def number_of_leading_zeros_for_large_x(x):
    if x == 0:
        return 64
    count = 1
    if (x >> 32) == 0:
        count = 33
        x = x << 32
    if (x >> 48) == 0:
        count += 16
        x = x << 16
    if (x >> 56) == 0:
        count += 8
        x = x << 8
    if (x >> 60) == 0:
        count += 4
        x = x << 4
    if (x >> 62) == 0:
        count += 2
        x = x << 2
    return count - (x >> 63)

# number of trailing '0's
def number_of_trailing_zeros(x):
    count = 0
    x = ~x & (x - 1)
    while x != 0:
        count += 1
        x = x >> 1

    return count

# for large number (> 3) of '0's
def number_of_trailing_zeros_binary_search(x):
    if x == 0:
        return 64
    count = 1
    if (x & 0xFFFFFFFF) == 0:
        count = 33
        x = x >> 32
    if (x & 0xFFFF) == 0:
        count += 16
        x = x >> 16
    if (x & 0xFF) == 0:
        count += 8
        x = x >> 8
    if (x & 0xF) == 0:
        count += 4
        x = x >> 4
    if (x & 3) == 0:
        count += 2
        x = x >> 2
    return count - (x & 1)

# detection of first L bits in succession (x: 64bit, L <= 64)
def successional_bits_detection(x, L):
    while (L > 1):
        s = L >> 1          # L // 2
        x = x & (x << s)
        L = L - s
    
    return number_of_leading_zeros_for_large_x(x)

##############################
# test code
print(parity(0b1100110100010111))
print(number_of_trailing_zeros(0b100000000))
print(number_of_trailing_zeros_binary_search(0b1000000000000))
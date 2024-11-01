# Range Maximum Queries
# A_1, ... , A_N :input data
# return max(A_l, ... , A_r-1)
# amount of calculation: ~ O(log(N))
#
#            1                 size(>= N): 2^k    
#      2           3           total size: 2^(k+1) - 1 
#   4     5     6     7        position: x  =>  cell: x + size - 1
#  8  9 10 11 12 13 14 15      cell: y  =>  above cell: y // 2
#  <--------2^k--------->             

import math 

class RangeMaximumQueries:
    
    # N: number of class of data
    # size: segment tree's size (number of cells in lowest column)
    def __init__(self, N):
        self.N = N
        siz = 1 << (math.ceil(math.log2(N)))
        self.size = siz
        self.cell = [0] * (2 * siz)

    def inputRMQ(self, position, input_value):
        cellnumber = position + self.size - 1
        self.cell[cellnumber] = input_value
        while cellnumber >= 2:
            cellnumber = cellnumber // 2
            self.cell[cellnumber] = max(self.cell[2*cellnumber], self.cell[2*cellnumber + 1])
    
    # [l, r): output semi open interval, [L, R): cell[cellnumber]'s interval
    def output_recursion(self, l, r, L, R, cellnumber):
        if (r <= L) or (R <= l):
            return -math.inf
        elif (l <= L) and (R <= r):
            return self.cell[cellnumber]
        else:
            m = (L + R) // 2
            L_max = self.output_recursion(l, r, L, m, cellnumber * 2)
            R_max = self.output_recursion(l, r, m, R, cellnumber * 2 + 1)
            return max(L_max, R_max) 

    def outputRMQ(self, l, r):
        R = self.size + 1
        return self.output_recursion(l, r, 1, R, 1)

############################################################################

class RangeMinimumQueries:
    def __init__(self, N):
        self.N = N
        siz = 1 << (math.ceil(math.log2(N)))
        self.size = siz
        self.cell = [0] * (2 * siz)

    def inputRmQ(self, position, input_value):
        cellnumber = position + self.size - 1
        self.cell[cellnumber] = input_value
        while cellnumber >= 2:
            cellnumber = cellnumber // 2
            self.cell[cellnumber] = min(self.cell[2*cellnumber], self.cell[2*cellnumber + 1])
    
    def output_recursion(self, l, r, L, R, cellnumber):
        if (r <= L) or (R <= l):
            return math.inf
        elif (l <= L) and (R <= r):
            return self.cell[cellnumber]
        else:
            m = (L + R) // 2
            L_min = self.output_recursion(l, r, L, m, cellnumber * 2)
            R_min = self.output_recursion(l, r, m, R, cellnumber * 2 + 1)
            return min(L_min, R_min) 

    def outputRmQ(self, l, r):
        R = self.size + 1
        return self.output_recursion(l, r, 1, R, 1)
    
#########################################################################

class RangeSumQueries:
    
    def __init__(self, N):
        self.N = N
        siz = 1 << (math.ceil(math.log2(N)))
        self.size = siz
        self.cell = [0] * (2 * siz)

    def inputRMQ(self, position, input_value):
        cellnumber = position + self.size - 1
        self.cell[cellnumber] = input_value
        while cellnumber >= 2:
            cellnumber = cellnumber // 2
            self.cell[cellnumber] = self.cell[2*cellnumber] + self.cell[2*cellnumber + 1]
    
    # [l, r): output semi open interval, [L, R): cell[cellnumber]'s interval
    def output_recursion(self, l, r, L, R, cellnumber):
        if (r <= L) or (R <= l):
            return 0
        elif (l <= L) and (R <= r):
            return self.cell[cellnumber]
        else:
            m = (L + R) // 2
            L_max = self.output_recursion(l, r, L, m, cellnumber * 2)
            R_max = self.output_recursion(l, r, m, R, cellnumber * 2 + 1)
            return L_max + R_max 

    def outputRMQ(self, l, r):
        R = self.size + 1
        return self.output_recursion(l, r, 1, R, 1)
import MapReduce
import sys
from collections import defaultdict

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    L = 5
    M = 5
    N = 5
    # key: document identifier
    # value: document contents
    matrix = record[0]
    row = record[1]
    col = record[2]
    value = record[3]
    if matrix == 'a':
        for k in range(0, N):
            mr.emit_intermediate((row, k), (matrix, row, col, value))
    elif matrix == 'b':
        for i in range (0, L):
            mr.emit_intermediate((i,col), (matrix, row, col, value))

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    # print key, list_of_values
    row = key[0]
    col = key[1]
    a_vals = [x for x in list_of_values if x[0] == 'a' ] 
    b_vals = [x for x in list_of_values if x[0] == 'b' ]
    total = 0    
    
    for a in a_vals:
        a_row = a[1]
        a_col = a[2]
        a_val = a[3]
        b_found = [x for x in b_vals if x[1] == a_col and x[2] == col]
        # print a, b_found
        if len(b_found) == 1:
            total += a_val*b_found[0][3]
    # print a_vals
    # print b_vals
    # print total
    mr.emit((row, col, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

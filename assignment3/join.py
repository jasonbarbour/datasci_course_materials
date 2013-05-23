import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    rtype = record[0]
    key = record[1]
    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #total = 
    #for v in list_of_values:
    #  total += v
    # total = list(set(list_of_values))
    line_items = []
    for value in list_of_values:
        if value[0] == 'order':
            order = value
        elif value[0] == 'line_item':
            line_items.append(value)
    for line_item in line_items:
        mr.emit((order + line_item))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

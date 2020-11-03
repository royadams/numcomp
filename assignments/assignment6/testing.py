import unittest
########################################
# Merge sort code
########################################

def merge_sort(x):
    result = []
    if len(x) < 2:
        return x
    mid = int(len(x)/2)
    y = merge_sort(x[:mid])
    z = merge_sort(x[mid:])
    while (len(y) > 0) or (len(z) > 0):
        if len(y) > 0 and len(z) > 0:
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
        elif len(z) > 0:
            result += z
            z = []
        else:
            result += y
            y = []
    return result
    

########################################
# Testing code
########################################

## Add code here ##

########################################
# Main
########################################
if __name__=="__main__":
    unittest.main()
from collections import Counter
def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    squared_counts = Counter(x*x for x in array1)
    b_counts = Counter(array2)
    return squared_counts == b_counts
       
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
print(comp(a, b))
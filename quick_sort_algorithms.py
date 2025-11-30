def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) - 1]
    left_arr = []
    right_arr = []
    for i in range(0, len(arr) - 1):
        if arr[i] < pivot:
            left_arr.append(arr[i])
        else:
            right_arr.append(arr[i])
    return [*quick_sort(left_arr), pivot, *quick_sort(right_arr)] 
print(quick_sort([3,5,7,9,2,6,1]))
# arr = [3,5,7,9,2,6,1]
# print(*arr)
from main import large_dataset

# sorting linearly
def sorting(arr):
    sorted_element = arr.copy()  # start with a copy of the original
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if sorted_element[i] > sorted_element[j]:
                # Swap if out of order
                sorted_element[i], sorted_element[j] = sorted_element[j], sorted_element[i]
    return sorted_element
print(sorting(large_dataset))

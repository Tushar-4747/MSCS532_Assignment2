#Quick Sort:

def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # This line needs to be indented properly
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]   
    return quick_sort(left) + middle + quick_sort(right)

#Testing example
example_list = [3, 6, 8, 10, 1, 2, 1]
sorted_list = quick_sort(example_list)
print("Sorted list:", sorted_list)
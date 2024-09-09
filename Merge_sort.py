#Merge_sort

def merge_sort(arr):
    # Base case: if the array has 0 or 1 element, it is already sorted
    if len(arr) <= 1:
        return arr


    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])


    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0


    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1


    result.extend(left[i:])
    result.extend(right[j:])
    return result
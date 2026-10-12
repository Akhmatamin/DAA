#Quick sort
#Time complexity O(n log n)
#Space O(n)

array = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left_arr = [x for x in arr[:-1] if x <= pivot]
    right_arr = [x for x in arr[1:] if x > pivot]

    left_arr = quick_sort(left_arr)
    right_arr = quick_sort(right_arr)

    return left_arr + [pivot] + right_arr

print(quick_sort(array))
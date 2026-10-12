#Merge Sort
#Time complexity O(n log n)
#Space O(n)

array = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n// 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)
    l_idx, r_idx = 0, 0
    left_len = len(left_arr)
    right_len = len(right_arr)
    sorted_arr = [0] * n
    i = 0

    while l_idx < left_len and r_idx < right_len:
        if left_arr[l_idx] < right_arr[r_idx]:
            sorted_arr[i] = left_arr[l_idx]
            l_idx += 1
        else:
            sorted_arr[i] = right_arr[r_idx]
            r_idx += 1
        i += 1

    while l_idx < left_len:
        sorted_arr[i] = left_arr[l_idx]
        l_idx += 1
        i += 1

    while r_idx < right_len:
        sorted_arr[i] = right_arr[r_idx]
        r_idx += 1
        i += 1

    return sorted_arr

print(merge_sort(array))




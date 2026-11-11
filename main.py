arr = [1, 3, 5, 7, 9, 11]

def search(arr, target):
  left, right = 0, len(arr) - 1

  while left <= right:
    mid = (left+right) // 2

    if arr[mid] == target:
      return mid

    elif target < arr[mid]:
      right = mid-1

    else:
      left = mid

  return -1

res = search(arr, 3)
print(res)
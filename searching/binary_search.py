def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == arr[mid]:
            return True
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


def binary_search_recursive(arr, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == arr[mid]:
            return True
        elif target < arr[mid]:
            return binary_search_recursive(arr, target, low=low, high=mid - 1)
        else:
            return binary_search_recursive(arr, target, low=mid + 1, high=high)


def find_the_closest_number(arr, target):
    low = 0
    high = len(arr) - 1
    closet_num = None
    min_diff = float("inf")

    if (len(arr)) == 0:
        return None
    if len(arr) == 1:
        return arr[0]

    while low <= high:
        mid = (low + high) // 2
        if mid + 1 < len(arr):
            min_diff_right = abs(arr[mid + 1] - target)
        if mid > 0:
            min_diff_left = abs(arr[mid - 1] - target)

        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closet_num = arr[mid - 1]

        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closet_num = arr[mid + 1]
        if arr[mid] > target:
            high = mid - 1
            if high < 0:
                return arr[mid]
        elif arr[mid] < target:
            low = mid + 1
        else:
            return arr[mid]
    return closet_num


arr = [1, 5, 23, 24, 28,45, 61, 70]
print(find_the_closest_number(arr,25))

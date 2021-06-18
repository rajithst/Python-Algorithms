def binary_search_iterative(arr,target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low+high)//2
        if target == arr[mid]:
            return True
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

def binary_search_recursive(arr,target,low,high):
    if low > high:
        return False
    else:
        mid = (low+high)//2
        if target == arr[mid]:
            return True
        elif target < arr[mid]:
            return binary_search_recursive(arr,target,low=low,high=mid-1)
        else:
            return binary_search_recursive(arr,target,low = mid+1,high = high)


arr = [1,2,3,4,5,6,7]
print(binary_search_recursive(arr,5,0,len(arr)-1))

def merge_sort(list_a):
    if len(list_a) > 1:
        mid = len(list_a) // 2
        left = list_a[:mid]
        right = list_a[mid:]
        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                list_a[k] = left[i]
                i += 1
            else:
                list_a[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            list_a[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            list_a[k] = right[j]
            j+=1
            k+=1

myList = [54,26,93,17,77,31,44,55,20]
merge_sort(myList)
print(myList)



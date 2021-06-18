def selection_sort(arr):
    """
    1) get the min value as current index
    2) find the minimum of remain sub array
    3) swap the values
    :param arr:
    :return:
    """

    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i],arr[min_index] = arr[min_index],arr[i]
    print(arr)

arr_input = [64, 25, 12, 22, 11]
selection_sort(arr_input)
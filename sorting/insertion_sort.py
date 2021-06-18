def insertion_sort(list_a):
    for i in range(1,len(list_a)):
        current_value = list_a[i]
        while i>0 and list_a[i-1] > current_value:
            list_a[i],list_a[i-1] = list_a[i-1],list_a[i]
            i = i -1
    return list_a


list_a = [4,1,3,46,23,135,6]
print(insertion_sort(list_a))

arrA = [2, 5, 4, 9, 10, 51, 24, 67]
arrB = [97, 15, 25, 27, 84]


def merge(arrA, arrB):
    merged_arr = []
    a = 0
    b = 0

    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr.append(arrA[a])
            a += 1
        else:
            merged_arr.append(arrB[b])
            b += 1
        # at this point, we have merged in all of the num_elementsfrom one of th earrays, but not the other

        # check both arrays to see if the pointer is still in range of its arrays
        if a < len(arrA):
            # arrA still has leftover num_elements push them to the merged arrays
            merged_arr.extend(arrA[a:])
        if b < len(arrB):
            merged_arr.extend(arrB[b:])


print(merge(arrA, arrB))


def merge_sort(arr):
    if len(arr) > 1:
        left = merge_sort(arr[0:len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])

        arr = merge(left, right)
    return arr


print(merge_sort(arrA))

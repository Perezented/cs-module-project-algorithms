def smallestMissingNum(arr, index=None):
    # if there is no index typed in, set an index and run again
    if index is None:
        index = 0
        smallestMissingNum(arr, index)
    # if the last item is the length of the array - 1
    if arr[-1] == len(arr) - 1:
        # return length, it is the next item
        return len(arr)
    # if the index is the arr[i],
    if index == arr[index]:
        # increment index, return the function
        index += 1
        return smallestMissingNum(arr, index)
    # else if the index is not the arr[index]
    else:
        # return the index, it's the missing number
        return index
    # last return
    return index


test2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test3 = [0, 1, 2, 3, 4, 5, 6, 10]
test1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(smallestMissingNum(test2))
print(smallestMissingNum(test3))
print(smallestMissingNum(test1))

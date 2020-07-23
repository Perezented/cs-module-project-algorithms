'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr, i=None, end=None):
    # Your code here
    # print(f'end: {end}')
    # print(f'array: {arr}')
    # print(f'index: {i}')
    # print('#####################')

    if i is None and end is None:
        i = 0
        end = 0
        moving_zeroes(arr, i, end)

    elif i >= 0:
        if end < -1 * len(arr):
            return arr
        if arr[i] != 0:
            if i == len(arr)-1:
                return arr
            else:
                i += 1
                return moving_zeroes(arr, i, end)
        elif arr[i] == 0:
            end -= 1
            # if arr[i + 1] > 0 and arr[i - 1] == 0:
            #     # print('hey')
            #     return arr
            arr.append(arr.pop(i))
            return moving_zeroes(arr, i, end)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

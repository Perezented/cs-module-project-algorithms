'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # Your code here
    if arr[0] == arr[1]:
        arr.pop()
        arr.pop()
    if arr[0] != arr[1]:
        if arr[0] + 1 != arr[2]:
            return arr[1]
            print(f'arr[1]: {arr[1]}')
        else:
            print(f'arr[0]: {arr[0]}')
            return arr[0]
    single_number(arr)


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

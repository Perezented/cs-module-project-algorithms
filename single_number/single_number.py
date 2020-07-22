'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # Your code here
    arr.sort()
    # print(arr)
    if len(arr) > 2:
        if arr[0] == arr[1]:
            arr.pop()
            arr.pop()
            single_number(arr)
        else:
            print(arr[0])
            print(arr[1])


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

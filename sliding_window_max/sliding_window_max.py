'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k, i=None, h=None, lis=None):
    # Your code here
    if i is None:
        i = 0
        h = i + k
        lis = []
    print(nums, k, i, h, lis)
    if h != len(nums)+1:
        lis.append(max(nums[i:h]))
        i += 1
        h += 1
        return sliding_window_max(nums, k,  i, h, lis)
    return lis


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

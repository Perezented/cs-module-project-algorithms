'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr, length=None):
    # Your code here

    # No length
    # then add length
    if length is None:
        length = len(arr)
    # length is 1,
    # return
    if length == 1:
        print(0)
        return
    # making of a left side and right side to multiply down
    left = [0] * length
    right = [0] * length
    # products array
    products = [0] * length
    # initial each side with 1
    left[0] = 1
    right[length - 1] = 1
    # apply items to the left
    for i in range(1, length):
        left[i] = arr[i - 1] * left[i - 1]
    # apply items to the right
    for j in range(length - 2, -1, -1):
        right[j] = arr[j + 1] * right[j + 1]
    # apply those multiplied items to the products array
    for i in range(length):
        products[i] = left[i] * right[i]
    # for i in range(length):
    #     print(products[i], end=' ')
    return products


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

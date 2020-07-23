'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n, filler=None):
    # Your code here
    print(n)
    print(filler)
    if filler is None:
        filler = []
        returnMe = 0
    if n <= 1:
        return 1
    if n == 2:
        return 2
    else:
        for num in range(n+1):
            filler.append(num)
        for x in filler:
            for y in filler:
                if x == n:
                    returnMe += 1
                if x + y == n:
                    returnMe += 1
    print(returnMe + 1)
    return returnMe + 1


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

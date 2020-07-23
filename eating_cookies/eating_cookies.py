'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n, cache=None):
    # Your code here
    if cache is None:
        cache = {}
    if n < 0:
        return 0
    if n == 0:
        return 1
    # check the cache to see if it holds the answer this branch is looking for
    elif n in cache:
        return cache[n]
    # if n == 2:
    #     return 2
    else:
        cache[n] = eating_cookies(
            n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
        return cache[n]

    # use a data structure to 'cache or save' answers taht some other branch has already done
    # save the n value as a key and the associated answer as its value in a dict
    # we will need to pass the dictionary to each call


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies), {}} ways for Cookie Monster to each {num_cookies} cookies")

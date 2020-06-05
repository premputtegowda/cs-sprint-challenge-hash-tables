def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    for i in a:
        cache[i] = i
   
    result = [key for key, value in cache.items() if key>0 and -key in cache]

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    for i in range(length):
        cache[weights[i]] = i
    
    for i in range(length):
        if (limit-weights[i]) in cache:
            return [cache[limit-weights[i]],i]




    return None

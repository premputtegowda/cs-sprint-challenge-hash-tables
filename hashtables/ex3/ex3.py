def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    count={}
    for array in arrays:
        # print("arry", array)
        for i in array:
           
            if i in count:
                count[i] +=1
            else:
                count[i] = 1
    
    result = [ key for key,value in count.items() if value >= len(arrays)]
    return result
    


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

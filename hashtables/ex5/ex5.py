# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache={}
    for file in files:

        file_key = file.split("/")
        if file_key[-1] not in cache:
            cache[file_key[-1]] = [file]
        else:
            cache[file_key[-1]].append(file)
    result=[]
    for query in queries:
        if query in cache:
        
            result = [*result, *cache[query]]
            print(result)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))

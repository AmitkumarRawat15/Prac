def smallestNum(arr):
    result = {}
    for i in range(len(arr)):
        if arr[i] > 0:
            if arr[i] not in result.keys():
                result[arr[i]] = 1
    index = 1
    while True:
        if (index not in result.keys()):
            return index
        index +=1

arr = [-5,-2,-3,-1,-4]
print(smallestNum(arr))
def binarySearch(list,target):
    """

    :param list: must be sorted value
    :param target:
    :return: list index position where target is
    if terget is not found the list return: None
    """
    firstPosition = 0
    lastPosition = len(list)-1

    # while firstPosition <= lastPosition:
    while firstPosition <= lastPosition:
        # print(firstPosition+lastPosition , firstPosition, lastPosition)
        midpoint = (firstPosition+lastPosition)//2
        # print(midpoint)
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            firstPosition = midpoint+1
        elif list[midpoint] > target:
            lastPosition = midpoint-1
    return None

def verify(result):
    if result is not None:

       return print("The target found in the lists index position : " + str(result))
    else:

        return  print("The target is not in the list")

# print(binarySearch.__doc__) #to read the document of a function
a = [1,2,3,4,5,6,7,8]

result = binarySearch( a , 10)
search = verify(result)
print(search)
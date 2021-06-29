def linearSearch(list,target):
    """

    :param list:
    :param target:
    :return index:
    if target is not in the list then return None
    """
    for index in range (0,len(list)):
        if list[index] == target:
            return index

    return None

def verify(result):
    if result is not None:
        print("The target found in the lists index position : " + str(result))
    else:
        print("The target is not in the list")

print(linearSearch.__doc__) #to read the document of a function
a = [5,3,9,50,20,499,100,400,30,500]

search = linearSearch( a , 400)
search = verify(search)
print(search)


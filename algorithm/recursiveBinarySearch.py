
def recursive_binary( list , target):
    print(list)
    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2
        if list[midpoint] == target:
            print("1st")
            return True
        elif list[midpoint] < target:
            print("2nd")
            return recursive_binary(list[midpoint+1:], target)
        elif list[midpoint] > target:
            print("3rd")
            return recursive_binary(list[:midpoint], target)

def verify(result):
    return result

a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

result = recursive_binary(a ,15)
check_result = verify(result)

print(result)

try:
    print("open")
    pass
except NameError as name:
    print(name)
except ZeroDivisionError as zero:
    print(zero)
finally:
    print("print")

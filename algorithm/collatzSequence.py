import sys
def collatz(number):
    reminder = number % 2
    quotient = number//2

    if number == 1:
        print(number)
        sys.exit()
    if reminder:
        print(number)
        return collatz(3*number + 1)
    else:
        print(number)
        return collatz(quotient)

while True:

    try:
        print("please pass integer only")
        user = int(input())
        collatz(user)
    except Exception:
        print("only input number except 0 ")
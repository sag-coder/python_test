import random,sys
ran = random.randint(1,20)
total_try=1
print("guessing the number between 1,20 : ")
while True:

    # print(ran)
    num = int(input())
    if num==ran:
        print("congo you crack it ")
        print("total_try: "+str(total_try))
        sys.exit()
    elif num < ran:
        print("guess higher")
        total_try = total_try + 1
        continue
    elif num > ran:
        print("guess lower")
        total_try = total_try + 1
        continue

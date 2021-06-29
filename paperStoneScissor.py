import sys, random
wins = 0
losses = 0
tie = 0

print("This is a paper scissor rock game")
while True:
    print('%s wins , %s losses, %s tie' % (wins, losses, tie))
    # print('{} wins , {} losses, {} tie'.format(wins, losses, tie)) #other syntex
    while True:
        print("chose (r)ock or (s)icssor or (p)aper or you can (e)xeit")
        userInput = input()
        if userInput == 'e':
            sys.exit()
        else:
            break


    randomNum = random.randint(1,3)
    if randomNum==1:
        computerInput = 'r'
    elif randomNum==2:
        computerInput = 's'
    elif randomNum==3:
        computerInput = 'p'
    print("computer choose : %s" % (computerInput))
    #wins case
    if (computerInput == 'p' and userInput == 's') or (computerInput == 's' and userInput == 'r') or (computerInput == 'p' and userInput== 'r'):
        wins=wins+1
        continue
    # tie case
    elif computerInput == userInput:
        tie= tie+1
        continue
    else:
        losses=losses+1
        continue

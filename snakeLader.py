import random
import sys
import time

snakeLaderBord = list(range(1, 101))
# print(snakeLaderBord)
player_1 = 1
player_1_flg = False
player_2 = 1
player_2_flg = False

print("****let's play ludo****")

def dice():
    event = random.randint(1, 6)
    return event
while True:
    time.sleep(0.1)
    print("-------------------------------------------------------------------")
    print("fst player turn:")
    input("please click enter")
    print("dice roll", end='')
    for i in range(5):
        time.sleep(0.5)
        print(".",end='')
    event = dice()
    print("\nfirst player dice %s" % event)
    time.sleep(0.5)
    if player_1_flg == False:
        if event == 1:
            time.sleep(0.5)
            print("first player start")
            print("board position %s" % snakeLaderBord[event-1])
            player_1_flg = True
    else:
        if len(snakeLaderBord) >= (player_1) and len(snakeLaderBord) >= player_1+event:
            player_1 = snakeLaderBord[player_1+event-1] #player 1 board position manupulation
            player_1 = snakeOrLadder(player_1)
            print("first player in board position %s" % player_1)
            if player_1 == 100:
                print("first player win ")
                sys.exit()
        else:
            print("first player board position %s" % player_1)
    time.sleep(0.1)
    print("-------------------------------------------------------------------")
    print("second player turn: ")
    input("please click enter...")
    print("dice roll", end='')
    for i in range(5):
        time.sleep(0.5)
        print(".", end='')
    event = dice()
    print("\nsecond player dice %s" % event)
    time.sleep(0.5)
    if player_2_flg == False:
        if event == 1:
            time.sleep(0.5)
            print("second player start")
            print("board position %s" % snakeLaderBord[event-1])
            player_2_flg = True
    else:
        if len(snakeLaderBord) >= (player_2) and len(snakeLaderBord)>=player_2+event:
            player_2 = snakeLaderBord[player_2 + event-1] #player 2 board position manupulation
            player_2 = snakeOrLadder(player_2)
            print("second player in board position %s" % player_2 )
            if player_2 == 100:
                print("second player win ")
                sys.exit()
        else:
            print("second player board position %s"%player_2)

    def snakeOrLadder(position):
        time.sleep(.5)
        if position==2:
            print("ladder 2")
            position=38
        elif position == 7:
            print("ladder 7")
            position = 14
        elif position == 8:
            print("ladder 8")
            position = 31
        elif position == 15:
            print("ladder 15")
            position = 26
        elif position == 28:
            print("ladder 28")
            position = 84
        elif position == 36:
            print("ladder 36")
            position = 44
        elif position == 51:
            print("ladder 51")
            position = 67
        elif position == 71:
            print("ladder 71")
            position = 91
        elif position == 78:
            print("ladder 78")
            position = 98
        elif position == 87:
            print("ladder 87")
            position = 94

        #snake---------------

        elif position == 16:
            print("snake 16")
            position = 6
        elif position == 46:
            print("snake 46")
            position = 25
        elif position == 49:
            print("snake 49")
            position = 11
        elif position == 62:
            print("snake 62")
            position = 19
        elif position == 64:
            print("snake 64")
            position = 60
        elif position == 74:
            print("snake 74")
            position = 53
        elif position == 92:
            print("snake 92")
            position = 88
        elif position == 95:
            print("snake 95")
            position = 75
        elif position == 99:
            print("snake 99")
            position = 80
        return position

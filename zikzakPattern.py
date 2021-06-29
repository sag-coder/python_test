import time
import sys
indent = 0
indentIncreasing = True
try:
    while True:
        print(' '*indent, end='')
        print('**********')
        time.sleep(1)
        if indentIncreasing:
            indent = indent+1
            #indent increasing
            if indent == 20:
                indentIncreasing = False
        else:
            #indent increasing
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()


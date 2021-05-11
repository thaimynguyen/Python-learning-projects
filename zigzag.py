#This program will create a back-and-forth, zigzag pattern until the user stops it by pressing the code editor's "STOP" button or by pressing CRTL-C

import time, sys

indent = 0 #Keep track of the number of white spaces before the 8 asterisks
indentIncreasing = True #Whether the indentation is increasing or not

try:
    while True: # The main program loop
        print(' ' * indent, end = '')
        print('********')
        time.sleep(0.1) # Pause for 1/10 of a second

        if indentIncreasing:
            # Increase the number of spaces in front
            indent += 1
            if indent == 20:
                #Change direction
                indentIncreasing = False
        else:
            indent -= 1
            if indent == 0:
                #Change direction
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()


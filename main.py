import os, sys, time

while True:
    option = int(input("\033[1;32m[1]\033[1;34m GUI\n\033[1;32m[2]\033[1;34m CLI\nInput: "))
    if option == 1:
        os.system("clear")
        for i in "\033[1;34mLAUNCHING GRAPHICAL USER INTERFACE...":
            print(i, end="")
            sys.stdout.flush()
            time.sleep(0.1)
        os.system("clear")
        os.system("python3 gui.py")
        break
    elif option == 2:
        os.system("clear")
        for i in "\033[1;34mLAUNCHING COMMAND-LINE INTERFACE...":
            print(i, end="")
            sys.stdout.flush()
            time.sleep(0.1)
        os.system("clear")
        os.system("python3 cli.py")
        break
    else:
        print("Wrong Input, please retry")
start_sign = False
stop_sign = True

while True:
    command = input("> ").upper()
    if command == "HELP":
        print('''
start - to start the car
stop - to stop the car
quit - to exit
        ''')

    elif command == "START":
        if start_sign:
            print("The car is already started!")
        else:
            print("Car started...Ready to go!")
            stop_sign = False
        start_sign = True

    elif command == "STOP":
        if stop_sign:
            print("The car is already stopped!")
        else:
            print("Car stopped.")
            start_sign = False
        stop_sign = True

    elif command == "QUIT":
        break
    else:
        print("I don't understand that...")




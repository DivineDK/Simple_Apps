command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("Car is already started!")
            print("How else can i help?")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
            print("How else can I help?")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
        How Can I Assist You...
Start - to start the car
stop - to stop the car 
quit - to quit""")
    elif command == "quit":
        print("Have a good day")
        break
    else:
        print("Sorry, I don't understand that!")
        print("I can only help you start or stop your car...")

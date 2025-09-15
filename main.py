print("Welcome to the Chatbot!")
name = input("What is your name: ")
print("Hello " + name + "!")
age = input("How old are you? ")
print("")
chating = True

while chating:
    print("How may I help you " + name + ".")
    print("1. end")
    print("2. placeholder")
    print("3. more placeholder")
    answer = input("Please choose a option number: ")
    if answer == "1":
        print("Goodbye " + name + "!")
        chating = False
    else:
        print("invalid option!")
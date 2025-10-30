# 3 bank company help with seting up account

accountType = {}
password = {}
accountNumber = {}
print("Welcome to the Chatbot!")
name = input("What is your name: ")
print("Hello " + name + "!")
age = input("How old are you? ")
print("")
chating = True

while chating:
    print("How may I help you " + name + ".")
    print("1. end")
    print("2. Check Account")
    print("3. Create Account")
    answer = input("Please choose a option number: ")
    print("")
    if answer == "1":
        print("Goodbye " + name + "!")
        chating = False
    elif answer == "2":
        print("Good chooice {name}!")
        while True:
            answer = input("Please insert account number")
            for i in accountNumber:
                if(answer == i):
                    print("")
    elif answer == "3":
        print("Good choice {name}!")
        while True:
            print("Here are some account options.")
            print("1. Checking account")
            print("2. Saving account") 
            print("3. Cancle")
            accountType = input("Can you please choose a option number: ")
            print("")
            if accountType == "1":
                print("Ok a checking account.")
                accountType.add("checking")
                break
            elif accountType == "2":
                print("Ok a saving account.")
                accountType.add("saving")
                accountNumber.add(accountNumber.Count() + 1000)
                print("")
                break
            elif accountType == "3":
                break
            else:
                print("invalid option")
    else:
        print("invalid option!")
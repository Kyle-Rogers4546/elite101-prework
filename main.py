# 3 bank company help with seting up account

accountType = ""
curAcountType = ""
madeAccountTypes = []
password = []
accountNumber = []
print("Welcome to the Chatbot!")
name = input("What is your name: ")
print("Hello " + name + "!")
age = input("How old are you? ")
print("")
chating = True

while chating:
    print("How may I help you " + name + ".")
    print("1. Create Account")
    print("2. Check Account")
    print("3. End")
    answer = input("Please choose a option number: ")
    print("")
    if answer == "3":
        print("Goodbye " + name + "!")
        chating = False
    elif answer == "2":
        print(f"Good chooice {name}!")
        while True:
            answer = input("Please insert account number: ")
            foundpassword = False
            for i in range(len(accountNumber)):
                if(answer == accountNumber[i]):
                    curpassword = input(f"Okay now please insert your account password: ")
                    if curpassword == password[i]:
                        print("Great here is your account information:")
                        print(f"Account Number: {accountNumber[i]}")
                        print(f"Password: {password[i]}")
                        print(F"Account Type: {madeAccountTypes[i]}")
                    else:
                        print("Sorry but that password does not much the account number.")
                    foundpassword = True
                    break
            if (not(foundpassword)):
                print("Sorry but we could not find that account number.")
            
            print("")
            break
    elif answer == "1":
        print(f"Good choice {name}!")
        while True:
            print("Here are some account options.")
            print("1. Checking account")
            print("2. Saving account") 
            print("3. Cancle")
            accountType = input("Can you please choose a option number: ")
            print("")
            if accountType == "1":
                print("Ok a checking account.")
                curAcountType = "checking"
                print("")
                password.append(input("Please create your account password: "))
                accountNumber.append(1000 + len(accountNumber))
                print("Ok all good here is your information")
                print(f"Account Number: {accountNumber[-1]}")
                print(f"Password: {password[-1]}")
                print(F"Account Type: {curAcountType}")
                answer = input("Is this information correct (y/n): ").upper()
                if(answer == "Y"):
                    print("Great!")
                    print(f"{name}, congrates on creating an account!")
                    print("Make sure to memorize your info!")
                    madeAccountTypes.append(curAcountType)
                else:
                    print("We hope you will try again!")
                    password.pop
                    accountNumber.pop
                print("")
                break
            elif accountType == "2":
                print("Ok a saving account.")
                curAcountType = "saving"
                print("")
                password.append(input("Please create your account password: "))
                accountNumber.append(1000 + len(accountNumber))
                print("Ok all good here is your information")
                print(f"Account Number: {accountNumber[-1]}")
                print(f"Password: {password[-1]}")
                print(F"Account Type: {curAcountType}")
                answer = input("Is this information correct (y/n): ").upper()
                if(answer == "Y"):
                    print("Great!")
                    print(f"{name}, congrates on creating an account!")
                    print("Make sure to memorize your info!")
                    madeAccountTypes.append(curAcountType)
                else:
                    print("We hope you will try again!")
                    password.pop
                    accountNumber.pop
                print("")
                break
            elif accountType == "3":
                break
            else:
                print("invalid option")
    else:
        print("invalid option!")
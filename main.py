# 3 bank company help with seting up account

# declare variables
accountType = ""
curAcountType = ""
madeAccountTypes = []
password = []
accountNumber = []
# intro print statments
print("Welcome to the Chatbot!")
name = input("What is your name: ") # get name
print("Hello " + name + "!")
age = input("How old are you? ") # get age
print("")
chating = True

while chating:
    # option print statments
    print("How may I help you " + name + ".")
    print("1. Create Account")
    print("2. Check Account")
    print("3. End")
    answer = input("Please choose a option number: ") # get user inputs
    print("")
    # end statments
    if answer == "3":
        print("Goodbye " + name + "!")
        chating = False # ends while loop
    elif answer == "2":
        print(f"Good chooice {name}!")
        while True:
            answer = int(input("Please insert account number: ")) # get user account number
            foundpassword = False
            for i in range(len(accountNumber)): # checks is account number right
                if(answer == accountNumber[i]):
                    curpassword = input(f"Okay now please insert your account password: ") #get user password
                    if curpassword == password[i]: # check if password right
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
            # option print statments
            print("Here are some account options.")
            print("1. Checking account")
            print("2. Saving account") 
            print("3. Cancle")
            accountType = input("Can you please choose a option number: ")
            print("")
            # option 1
            if accountType == "1":
                print("Ok a checking account.")
                curAcountType = "checking"
                print("")
                password.append(input("Please create your account password: ")) # save info
                accountNumber.append(1000 + len(accountNumber)) # save info
                print("Ok all good here is your information")
                print(f"Account Number: {accountNumber[-1]}")
                print(f"Password: {password[-1]}")
                print(F"Account Type: {curAcountType}")
                answer = input("Is this information correct (y/n): ").upper()
                if(answer == "Y"):
                    print("Great!")
                    print(f"{name}, congrates on creating an account!")
                    print("Make sure to memorize your info!")
                    madeAccountTypes.append(curAcountType) # save info
                else:
                    print("We hope you will try again!")
                    password.pop # removes info
                    accountNumber.pop # removes info
                print("")
                break
            # option 2
            elif accountType == "2":
                print("Ok a saving account.")
                curAcountType = "saving"
                print("")
                password.append(input("Please create your account password: ")) # saves info
                accountNumber.append(1000 + len(accountNumber))  # saves info
                print("Ok all good here is your information")
                print(f"Account Number: {accountNumber[-1]}")
                print(f"Password: {password[-1]}")
                print(F"Account Type: {curAcountType}")
                answer = input("Is this information correct (y/n): ").upper()
                if(answer == "Y"):
                    print("Great!")
                    print(f"{name}, congrates on creating an account!")
                    print("Make sure to memorize your info!")
                    madeAccountTypes.append(curAcountType) # saves info
                else:
                    print("We hope you will try again!")
                    password.pop # removes info
                    accountNumber.pop # removes info
                print("")
                break
            elif accountType == "3":
                break
            else:
                print("invalid option")
    else:
        print("invalid option!")
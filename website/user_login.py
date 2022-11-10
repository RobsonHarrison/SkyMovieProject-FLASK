import mysql.connector

userDb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    db="user_login"
)
mycursor = userDb.cursor()
loggedIn = False

def loginuser(username, password):

    # check password matches against username
    mycursor.execute(f'SELECT _password FROM users WHERE user_name = "{username}"')
    collect = mycursor.fetchone()
    if password == collect[0]:
        mycursor.execute(f'SELECT first_name FROM users WHERE user_name = "{username}"')
        nameWelcome = mycursor.fetchone()
        output = nameWelcome[0]
        # print(f'Welcome {nameWelcome[0]}, You are now logged in!')
        loggedIn = True
        return output

        # print("Incorrect username or password")






def setPassword(password):

    valid = "no"
    while valid == "no":
        password = input("Please enter password: ")
        capsList = []
        lowerList = []
        numberList = []
        symbolList = []
        print("***********************************************************************")
        if len(password) >= 8:
            for caps in password:
                if caps.isupper():
                    charValid = True
                    capsList.append(charValid)
            for lower in password:
                if lower.islower():
                    charValid = True
                    lowerList.append(charValid)
            for number in password:
                if number.isnumeric():
                    charValid = True
                    numberList.append(charValid)
            for symbol in password:
                if symbol in "[@_!#£$%^&*()<>?/|}{~:]":
                    charValid = True
                    symbolList.append(charValid)
            fullCheck = []
            x = any(capsList)
            if x == True:
                #print(f"You have included Capital letters in your password")
                fullCheck.append(x)
            else:
                print(f"\033[91mYou have not included any capitals in your password\033[0m")
                fullCheck.append(x)
            y = any(lowerList)
            if y == True:
                #print(f"You have included lower case letters in your password")
                fullCheck.append(y)
            else:
                print(f"\033[91mYou have not included any lower case in your password\033[0m")
                fullCheck.append(y)
            z = any(numberList)
            if z == True:
                #print(f"You have included numbers in your password")
                fullCheck.append(z)
            else:
                print(f"\033[91mYou have not included any numbers in your password\033[0m")
                fullCheck.append(z)
            w = any(symbolList)
            if w == True:
                #print(f"You have included symbols in your password")
                fullCheck.append(w)
            else:
                print(f"\033[91mYou have not included any symbols in your password\033[0m")
                fullCheck.append(w)
            complete = all(fullCheck)
            print("***********************************************************************")
            if complete:
                print("\033[92mWell done, your password is valid!\033[0m")
                valid = "yes"
            else:
                print("\033[91mYour password is missing something, try again\033[0m")
            print("***********************************************************************")
        else:
            print("\033[91mYour password is not long enough, please enter 8 characters or more\033[0m")
            print("***********************************************************************")
    while True:
        passwordConfirm = input("Please re-enter your password: ")
        if passwordConfirm != password:
            print("Passwords do not match!!")
        else:
            break
    print(f'Your password has been set!')
    return password
import mysql.connector

userDb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    db="skymovie_christmas"
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
        # Return name to show welcome message
        loggedIn = True
        return output

def setPassword(password, passwordConfirm):
    valid = "no"
    while valid == "no":
        # Take password and run through check to ensure contains capital, lower, number, symbol and over 8 characters
        capsList = []
        lowerList = []
        numberList = []
        symbolList = []
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
                #print(f"\033[91mYou have not included any capitals in your password\033[0m")
                fullCheck.append(x)
            y = any(lowerList)
            if y == True:
                #print(f"You have included lower case letters in your password")
                fullCheck.append(y)
            else:
                #print(f"\033[91mYou have not included any lower case in your password\033[0m")
                fullCheck.append(y)
            z = any(numberList)
            if z == True:
                #print(f"You have included numbers in your password")
                fullCheck.append(z)
            else:
                #print(f"\033[91mYou have not included any numbers in your password\033[0m")
                fullCheck.append(z)
            w = any(symbolList)
            if w == True:
                #print(f"You have included symbols in your password")
                fullCheck.append(w)
            else:
                #print(f"\033[91mYou have not included any symbols in your password\033[0m")
                fullCheck.append(w)
            complete = all(fullCheck)
            if complete:
                #print("\033[92mWell done, your password is valid!\033[0m")
                valid = "yes"
            else:
                # Password is missing something, need to send error and restart
                error = "Password not valid"
                return error
        else:
            error = "Password not valid"
            return error
    while True:
        if passwordConfirm != password:
            error = "Passwords do not match!!"
            return error
        else:
            break
    #print(f'Your password has been set!')
    return password

def newUser(firstname, lastname, email, userName, password, passwordConfirm):
    # New user
    # Choose a username - must be unique

    # Check database to ensure username is unique
    mycursor.execute("select user_name from users")
    nameCheck = mycursor.fetchall()
    final_result = [list(i) for i in nameCheck]
    for x in final_result: # Could use try: except:
        if userName not in x:
            continue
        else:
            # If username already in use then start newUser function again
            error = "Username already exists!!!"
            return error
    # If username is usable then run create password function, returns set password
    sendPassword = setPassword(password, passwordConfirm)
    # Once username set collect email, and name

    # Send collected info to database
    mycursor.execute(f'insert into users(user_name, _password, email_address, first_name, last_name) values("{userName}", "{sendPassword}", "{email}", "{firstname}", "{lastname}");')
    userDb.commit() # Save in database
    # return username back to calling function for use on page
    return firstname
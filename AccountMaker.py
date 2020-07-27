import csv

# Creates new user
def newUser(user, password, first_name, last_name):
    with open('accounts.csv', 'a', newline="") as file:
        writer = csv.writer(file)
        writer.writerow([user, password, first_name, last_name])

# Check if username is already taken
def checkUser(user):
    found = False
    with open('accounts.csv', 'r') as file:
        accounts = csv.reader(file)

        for row in accounts:
            if(row[0] == user):
                found = True
    return found

# Login Method
def oldUser(user, password):
    found = False
    with open('accounts.csv', 'r') as file:
        accounts = csv.reader(file)

        for row in accounts:
            if(row[0] == user):
                if(row[1] == password):
                    found = True
                    break
    return found

# Login Welcome Message
def welcome(user):
    fname = ""
    lname = ""
    with open('accounts.csv', 'r') as file:
        accounts = csv.reader(file)

        for row in accounts:
            if row[0] == user:
                fname = row[2]
                lname = row[3]
    return("Login Successful \n Welcome " + fname + ' ' + lname)


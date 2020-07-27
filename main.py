# code made by https://github.com/treywaevin 

from tkinter import *
from AccountMaker import *

# Reveals Registration Screen
def showReg():
    # Create new frame
    regFrame.pack(fill='both', expand=1)

    # Hide Login Widgets
    nameLabel.lower()
    passwordLabel.lower()
    nameEntry.lower()
    passwordEntry.lower()
    loginButton.lower()
    resetButton.lower()
    registerButton.lower()
    registerLabel.lower()
    
    # Position Widget
    fName.place(x=150, y=10)
    lName.place(x=150, y=40)
    newName.place(x=150, y=70)
    newPass.place(x=150, y=100)
    fNameE.place(x=220, y=10)
    lNameE.place(x=220, y=40)
    newNameE.place(x=220, y=70)
    newPassE.place(x=220, y=100)
    registerButton1.place(x= 185, y=130)
    returnLogin.place(x=0, y= 25)
    returnButton.place(x=25, y= 45)

# Removes Registration Screen
def delFrame():
    regFrame.pack_forget()

# Creates popup window
def popupmsg(msg):
    popup = Tk()
    popup.wm_title('Alert!')
    popup.geometry('200x100')
    popLbl = Label(popup, text = msg).pack(side = "top", fill = "x", pady=10)
    exitBtn = Button(popup,text='Okay', command=popup.destroy).pack(side='bottom')
    popup.mainloop


# Sends info to AccountMaker in order to register account
def register():
    print("succeses")
    # Assign iinfo to variables
    first_name = fNameE.get()
    last_name = lNameE.get()
    username = newNameE.get()
    password = newPassE.get()
    if (len(first_name) != 0 and len(last_name) != 0 and len(username) != 0 and len(password) != 0):
        if checkUser(username) is False:
            newUser(username, password, first_name, last_name)
            delFrame()
            # Clears entries
            fNameE.delete(0, END)
            lNameE.delete(0, END)
            newNameE.delete(0, END)
            newPassE.delete(0, END)
            popupmsg("Account registered! Please Login")
        else:
            popupmsg("Username already taken")
    else: 
        popupmsg("Please fill out \n all credentials")

# Sends credentials to AccountMaker
def login():
    username = nameEntry.get()
    password = passwordEntry.get()
    if oldUser(username, password):
        popupmsg(welcome(username))
    else:
        popupmsg("Login Failed \n User or password incorrect")

# Resets all fields
def reset():
    nameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    


#Create GUI
root = Tk()
root.title('Login System')
root.geometry("500x200")

# Create Frames
regFrame = Frame(root)
#logFrame = Frame(root)

#Login Widgets:
label = Label(root, text = "Simple Python Login System", bg="cyan", font=(None, 20), height=1)
registerLabel = Label(root, text = "New User?", font=(None, 10))
nameLabel = Label(root, text="Username", )
passwordLabel = Label(root, text="Password")
nameEntry = Entry(root)
passwordEntry = Entry(root, show="*")
loginButton = Button(root, text="Login", width=11, command=login)
resetButton = Button(root, text="Reset", width=11, command=reset)
registerButton = Button(root, text="Register", width=6, command=showReg)

#Register Widgets
fName = Label(regFrame, text='First Name')
lName = Label(regFrame, text='Last Name')
newName = Label(regFrame, text='Username')
newPass = Label(regFrame, text='Password')
returnLogin = Label(regFrame, text = 'Already have an account?')
fNameE = Entry(regFrame)
lNameE = Entry(regFrame)
newNameE = Entry(regFrame)
newPassE = Entry(regFrame, show="*")
returnButton = Button(regFrame, text = 'Login', command=delFrame)
registerButton1 = Button(regFrame, text='Register Account', width= 15, command=register)
 
#Position Widgets
label.pack(fill=X)
registerLabel.place(x=0, y=50)
nameLabel.place(x=150, y=80)
passwordLabel.place(x=150, y=120)
nameEntry.place(x=220, y=80)
passwordEntry.place(x=220, y=120)
loginButton.place(x=150, y=160)
resetButton.place(x=280, y=160)
registerButton.place(x=5, y=75)

#logFrame.pack(fill='both', expand=1)

    
root.mainloop()













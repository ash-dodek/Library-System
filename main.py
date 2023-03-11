from LibActions.addBook import *
from LibActions.getBooks import *
from LibActions.issueBook import *
from LibActions.returnBook import *
from LoginRegister.register import *
from LoginRegister.login import *
import os


os.system('cls')
print("-----------------------Welcome to the Library,Choose an appropriate number-----------------------")
print("1 => Register Yourself")
print("2 => Login By your Username and password")
# print("3 => Log Out\n")
isInt = False
someChoice = 0
while isInt == False:
    try:
        someChoice = int(input("Enter your choice: "))
        isInt = True
        if someChoice > 4 or someChoice < 1:
            raise ValueError
    except ValueError:
        isInt = False
        print("Please enter a correct choice")
del isInt
os.system('cls')

if someChoice == 1:
    isRegistered = False
    while isRegistered == False:
        uName = input("Enter the username you want to keep:\n")
        pwd = input("Enter the passsword you want to keep:\n")
        newUser = User(uName, pwd)
        if newUser.feedInData() == True:
            os.system('cls')
            isRegistered = True
            print(f"\t\t\t\t\tSuccesfully registered as {uName}")
        else:
            isRegistered = False

elif someChoice == 2:
    isLoggedIn = False
    while isLoggedIn != True: 
        uName = input("Enter your Registered Username: ")
        pwd = input("Enter your password: ")
        output = login(uName, pwd)
        if output == True:
            isLoggedIn = True
            os.system('cls')
            print(f"\t\t\t\t\tSuccessfully logged in as {uName}")


        elif output == "pwError":
            print(f"The password you entered \"{pwd}\" is wrong, try again")
            isLoggedIn = False

        elif output == "uError":
            print(f"The entered username \"{uName}\" is not found in registered users")
            isLoggedIn = False
        del output,pwd
# elif someChoice == 3:
#     uname = input("Enter name: ")
    # pass

rerun = True
while rerun == True:
    print(f"---------------Welcome to the Library {uName},Choose an appropriate number---------------")
    print("1 => Add a Book to Library")
    print("2 => Check available boooks in library")
    print("3 => Issue a Book From the library")
    print("4 => Return a book the Library")
    print("5 => Exit")


    isInt = False
    while isInt == False:
        try:
            choice = int(input("Enter your choice: "))
            isInt = True
        except ValueError:
            isInt = False
            print("Please enter a correct choice")
    del isInt
    
    if choice == 1:
        os.system('cls')
        BookName = input("Enter the name of the Book: ")
        author = input("Enter the author of the Book: ")
        newBook = Book(BookName, author)
        if newBook.feedInData():
            pass

        else: 
            print("Some error occured")
            
        othChoice = input("Do you want to run the program again?").lower()
        if othChoice == 'yes' or othChoice == "y":
            rerurn = True
            os.system('cls')
        else:
            rerun = False


    elif choice == 2:
        os.system('cls')
        getAvailableBooks()
        print("\n")

        othChoice = input("Do you want to run the program again?").lower()
        if othChoice == 'yes' or othChoice == "y":
            rerurn = True
            os.system('cls')
        else:
            rerun = False

    elif choice == 3:
        os.system('cls')
        bName = input("Enter name of the Book You want to issue:\n")
        if issueBook(bName):
            print(f"Successfully Issued {bName}")
        else:
            print("Book is already issued or it doesn't exist")

        othChoice = input("Do you want to run the program again?").lower()
        if othChoice == 'yes' or othChoice == "y":
            rerurn = True
            os.system('cls')
        else:
            rerun = False

    elif choice == 4:
        os.system('cls')
        bName = input("Enter name of the Book You want to return:\n")
        if returnBook(bName):
            print(f"Successfully returned the {bName}")
        othChoice = input("Do you want to run the program again?").lower()
        if othChoice == 'yes' or othChoice == "y":
            rerurn = True
            os.system('cls')
        else:
            rerun = False

    elif choice == 5:
        break

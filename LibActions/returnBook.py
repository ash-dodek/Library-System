
def isAvailableToReturn(name):
    name = name.lower()
    Books = open("Data/availBooks.csv", "r")
    BookList = Books.readlines()
    for i in range(len(BookList)):
        newlist = BookList[i].split(",")
        if newlist[0].lower() == name:
            if newlist[2] == "True":
                return True
            else:
                print(f"{name} is not issued by anyone, how can you return it?")
                return False
    print(f"{name} was never in the library")

def returnBook(name):
    Bname = name.lower()
    if(isAvailableToReturn(Bname)==True):
        BookName = name.lower()
        Books = open("Data/availBooks.csv", "r")
        BookList = Books.readlines()
        Books.close()
        for i in range(len(BookList)):
            CurrBook = BookList[i].split(",")
            if CurrBook[0].lower() == BookName:
                CurrBook[2] = "False"

                BookList[i] = ",".join([str(elem) for elem in CurrBook])
                BookWriter = open(r"Data/availBooks.csv", "w")
                BookWriter.writelines(BookList)
                BookWriter.close()
                return True

            else:
                pass
        else:
            return False


        
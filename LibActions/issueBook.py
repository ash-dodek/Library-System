def issueBook(name):
    BookName = name.lower()
    Books = open("Data/availBooks.csv", "r")
    BookList = Books.readlines()
    Books.close()

    if isAvailable(BookName)==True:
        for i in range(len(BookList)):
            CurrBook = BookList[i].split(",")
            if CurrBook[0].lower() == BookName:
                CurrBook[2] = "True"

                BookList[i] = ",".join([str(elem) for elem in CurrBook])
                BookWriter = open(r"Data/availBooks.csv", "w")
                BookWriter.writelines(BookList)
                BookWriter.close()
                return True

            else:
                pass

    else:
        return False


def isAvailable(name):
    name = name.lower()
    Books = open("Data/availBooks.csv", "r")
    BookList = Books.readlines()
    for i in range(len(BookList)):
        newlist = BookList[i].split(",")
        if newlist[0].lower() == name:
            if newlist[2] == "False":
                return True
            else:
                return False
    Books.close()

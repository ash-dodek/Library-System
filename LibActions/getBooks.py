def getAvailableBooks():
    Books = open(r"Data/availBooks.csv", "r")
    BookList = Books.readlines()
    for i in range(len(BookList)):
        thisLine = BookList[i].split(",")
        print(f"Book Name: {thisLine[0]}")
        print(f"Author Name: {thisLine[1]}")
        print("-------")
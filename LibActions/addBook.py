class Book:
    def __init__(self, bName, auth) -> None:
        self.BookName = bName
        self.Author = auth
        self.IfIssued = False
        self.issueID = None


    def feedInData(self):
        DataFile = open(r"Data/availBooks.csv", "a")
        DataFile.write(f"{self.BookName},{self.Author},{self.IfIssued},{self.issueID}\n")
        DataFile.close()
        print(f"{self.BookName} written by {self.Author} added succesfully in Library")
        return True

    # feedInData()    

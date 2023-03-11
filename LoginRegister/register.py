class User:
    def __init__(self, uName, pwd):
        self.userName = uName
        self.password = pwd

    def feedInData(self):
        if checkIfExists(self.userName) != True:
            DataFile = open(r"Data/userDetails.csv", "a")
            DataFile.write(f"{self.userName},{self.password}\n")
            DataFile.close()
            return True
        else:
            return False


def checkIfExists(userName):
    DataFile = open(r"Data/userDetails.csv", "r")
    allLines = DataFile.readlines()
    for i in range(len(allLines)):       
        currLine = allLines[i].split(",")
        if currLine[0] == userName:
            print(f"Someone with User Name \"{userName}\" already exists in the library, please choose another UserName")
            return True
        else:
            pass
    
    return False


def login(userName, pwd):
    pwd = pwd + "\n"
    DataFile = open(r"Data/userDetails.csv", "r")
    uDetails = DataFile.readlines()
    DataFile.close()
    for i in range(len(uDetails)):
        currUser = uDetails[i].split(",")
        if currUser[0] == userName:
            if currUser[1] == pwd:
                return True
            else:
                return "pwError"
        # else:
    return "uErrr"
    # print(f"The username {userName} could not be found in registered users")
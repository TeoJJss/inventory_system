#Ng Jan Hwan
#TP068352

def user_authentication() -> str:
    # Assume "userdata.txt" is placed in the same directory as code file
    # Assume that credentials in "userdata.txt" are correct

    # Initialize
    filename="userdata.txt"
    credentials=username=password=""
    
    while True:
        # Opening file and taking credentials from file
        with open(filename, 'r') as file:
            credentials = file.readlines()

        for ind, data in enumerate(credentials):
            credentials[ind] = data.rstrip().split("\t")

        # Asking for user input
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()
        for line in credentials:
            if line[1] == username and line[2] == password:
                role = line[3]
                print("Authentication successful. User is a(n)", role)
                return role
        else:
            print("Authentication failed! Please login again.")

role=user_authentication()
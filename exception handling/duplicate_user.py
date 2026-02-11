class DuplicateUser(Exception):
    def __int__(self,message):
        super().__int__(message)

Username=input("Enter a username: ")
Password="Admin"

try:
    if Username=="Admin" or Username=="admin":
        raise DuplicateUser("Username already used.")
    else:
        print("Valid username")
except DuplicateUser as d:
    print("enter another username.",d)


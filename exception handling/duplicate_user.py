class DuplicateUser(Exception):
    def __int__(self,message):
        super.__int__(message)

Username="Admin"
Password="Admin"

try:
    if Username=="Admin":
        raise DuplicateUser("Username already used.")
    else:
        print("Valid username")
except DuplicateUser as d:
    print("enter another username.",d)
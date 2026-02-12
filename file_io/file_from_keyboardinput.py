def Keyboardtofile():
    file = open("../files/keyboard.txt","w")
    t = input("Enter your message: ")

    while(t!="quit"):
        file.write(t)
        file.write(" ")
        t = input(" ")
    file.close()
Keyboardtofile()
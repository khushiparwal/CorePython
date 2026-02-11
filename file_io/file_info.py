def fileinfo():
    f1 = open("../files/hello.txt","r")
    print("File name: ",f1.name)
    print("File mode: ",f1.mode)
    print("Is file closed: ",f1.closed)
    f1.close()
    print("After closing, is file closed now:",f1.closed)
fileinfo()
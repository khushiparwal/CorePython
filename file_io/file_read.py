def readfile():
    f1 = open("../files/hello.txt","r")
    t = f1.read()
    print(t)
    f1.close()

readfile()
def readfile():
    file = open("C:\Users\RST\Desktop\Shape.txt","r")
    t = file.read()
    print(t)
    file.close()
readfile()
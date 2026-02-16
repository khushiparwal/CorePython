def readfile():
    file = open("E:\shape.txt","r")
    t = file.read()
    print(t)
    file.close()


readfile()
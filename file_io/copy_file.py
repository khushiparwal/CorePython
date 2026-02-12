import shutil
source=r"E:\shape.txt"
target = r"E:\add\shape1.txt"

shutil.copyfile(source, target)
print("File copied from"+source+"to"+target)


import pickle
from write_objectfile import Employee

with open("../files/Employee.txt","rb") as file:
    obj = pickle.load(file)
    print("Employee info:")
    obj.display()
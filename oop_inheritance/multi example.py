class Math():
    def get_mth(self,mth=0):
        self.mth = mth
        return self.mth

class Science():
    def get_sci(self,sci=0):
        self.sci = sci
        return self.sci

class English():
    def get_eng(self,eng=0):
        self.eng = eng
        return self.eng

class School(Math,Science,English):
    def display(self):
        return self.mth+self.eng+self.sci

s1 = School()
print("Math marks:",s1.get_mth(85))
print("Science marks:",s1.get_sci(92))
print("English marks:",s1.get_eng(78))
print("Total marks:",s1.display())


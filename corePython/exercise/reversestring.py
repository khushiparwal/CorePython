s = "khushi"
s1 = ""

for i in range(len(s)-1,-1,-1):
    s1 = s1+s[i]
print(s1)

name = "khushi parwal"
w = name.split()
for word in w:
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    print(reversed_word, end=" ")



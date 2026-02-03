n = "hello world"
for letter in "abcdefghijklmnopqrstuvwxyz":
    c = 0
    for ch in n:
        if letter == ch:
            c += 1
    if c>0:
        print(letter,":",c)
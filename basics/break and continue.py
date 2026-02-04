s = "hello world"
for ch in s:
    if ch=="l":
        break
    print(ch,end="")
print()
for ch in s:
    if ch=="l":
        continue
    print(ch,end="")
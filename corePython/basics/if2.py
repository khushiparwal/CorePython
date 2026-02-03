d1 = {"January":31,"february":28,"march":31,"april":30,"may":31,"june":30,"july":31,
      "august":31,"september":30,"october":31,"november":30,"december":31}

i = 0
for i in range(len(d1)):
    if d1[i] == 31:
        print(d1[i])
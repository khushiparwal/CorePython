import re
import os
def readline():
    input_file = open('../files/mail.txt','r')
    output_file = open('../files/filtered_mail.txt','w')

    for line in input_file:
        if (re.search('@gmail.com',line)):
            output_file.write(line)
    input_file.close()
    output_file.close()

readline()

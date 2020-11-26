from re import search

file = open("test.cpp","r")
for line in file:
    if search("printf", line):
        s = line.split("(")[1].split(")")
        print(s)
        f = open("text.py","w")
        f.write("print("+s[0]+")")

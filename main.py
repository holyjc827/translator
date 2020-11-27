from re import search

file = open("test.cpp","r")
for line in file:
    if search("printf", line):
        s = line.split("(")[1].split(")")
        with open('text.py', 'a') as l:
            l.writelines("%s\n" % ("print("+s[0]+")"))
    if search(r'\bint\b', line): #word boundary to check the exact word 'int'
        if search("=", line):
            f = line.split("=")
            name = f[0].split(" ")[-1]
            assignment = f[1].split(";")[0]
            with open('text.py', 'a') as l:
                l.writelines("%s\n" % (name + " = int(" + assignment + ")"))
        elif search(";\n", line):
            f = line.split(" ")[-1].strip(";\n")
            with open('text.py', 'a') as l:
                l.writelines("%s\n" % (f+ " = ' '"))
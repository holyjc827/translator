from re import search

class Translator:
    def printf(self, line, file_out):
        if search("printf", line):
            s = line.split("(")[1].split(")")
            with open(file_out, 'a') as l:
                    l.writelines("%s\n" % ("print(" + s[0] + ")"))
    def int_func(self, line, file_out):
        if search(r'\bint\b', line):  # word boundary to check the exact word 'int'
            if search("=", line):
                f = line.split("=")
                name = f[0].split("int")[1].strip(" ")
                assignment = f[1].split(";")[0].strip(" ")
                with open(file_out, 'a') as l:
                    l.writelines("%s\n" % (name + " = int(" + assignment + ")"))
            elif search(";\n", line):
                f = line.split(" ")[-1].strip(";\n")
                with open(file_out, 'a') as l:
                    l.writelines("%s\n" % (f + " = ' '"))

    def loop(self, line, file_out):
        if search('while', line):
            f = line.split('(')[1].strip(')\n')
            if f == "true":
                f = "True"
            elif f == "false":
                f == "False"
            with open(file_out, 'a') as l:
                l.writelines("%s\n" % ("while " + f + " : "))

if __name__ == '__main__':
    app = Translator()
    file = open("test.cpp","r")
    for line in file:
        app.printf(line, "text.py")
        app.int_func(line, "text.py")
        app.loop(line, "text.py")
    file.close()
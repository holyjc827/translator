from re import search

class Translator:
    def __init__ (self):
        self.indent = "   "
        self.indentNum = 0

    def printf(self, line, file_out):
        if search("printf", line):
            s = line.split("(")[1].split(")")
            with open(file_out, 'a') as l:
                    l.writelines("%s\n" % ("print(" + s[0] + ")"))
            return True
        return False

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
            return True
        return False

    def loop(self, line, file_out):
        if search('while', line) != None:
            f = line.split('(')[1].strip(')\n')
            if f == "true":
                f = "True"
            elif f == "false":
                f == "False"
            with open(file_out, 'a') as l:
                l.writelines("%s\n" % (self.indent*self.indentNum + "while " + f + " : "))
            self.indentNum += 1
            return True
        return False

    def conditional(self, line, file_out):
        if search('if', line):
            f = line.split('(')[1].strip(')\n')
            with open(file_out, 'a') as l:
                l.writelines("%s\n" % (self.indent*self.indentNum + "if " + f + " : "))
            self.indentNum += 1
            return True
        return False

    def none(self, line, file_out):
        if search(';', line):
            f = line.split(';')[0].split()
            newline = f[0]
            for word in range(0,len(f)-1):
                newline = newline + " " + str(word)
            with open(file_out, 'a') as l:
                l.writelines("%s\n" % (self.indent*self.indentNum + newline))

    def closing(self, line, file_out):
        if search('}', line) != None:
            self.indentNum -= 1
            f = line.split(';')[0].split()
            newline = ""
            for word in f:
                word = word.split()[0]
                newline = newline + " " + word
            with open(file_out, 'a') as l:
                c = newline.split('}')[0].strip(')\n')
                l.writelines("%s\n" % (self.indent*self.indentNum + c))
            return True
        return False

    def opening(self, line, file_out):
        if search('{', line) != None:
            with open(file_out, 'a') as l:
                c = line.split('{')[1].strip(')\n')
                l.writelines("%s\n" % (self.indent*self.indentNum + c))
            return True
        return False 

    def importing(self, line, file_out):
        if search('#include', line):
            if search('<', line):
                with open(file_out, 'a') as l:
                    l.writelines("%s\n" % (self.indent*self.indentNum))
                return True
        return False

    def vector(self, line, file_out):
        if search ("std::vector", line):
            with open(file_out, 'a') as l:
                c = line.split('>')[1].split()[0].split(';')[0]
                print(c)
                l.writelines("%s\n" % (self.indent * self.indentNum + c + " = []"))
            return True
        return False

if __name__ == '__main__':
    app = Translator()
    file = open("test.cpp","r")
    for line in file:
        if app.importing(line, "text.py") == True:
            continue
        elif app.vector(line, "text.py") == True:
            continue
        elif app.printf(line, "text.py") == True:
            continue
        elif app.int_func(line, "text.py") == True:
            continue
        elif app.conditional(line, "text.py") == True:
            continue
        elif app.loop(line, "text.py") == True:
            continue
        elif app.opening(line, "text.py") == True:
            continue
        elif app.closing(line, "text.py") == True:
            continue
        else:
            app.none(line, "text.py")
    file.close()
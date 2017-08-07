#!/usr/bin/env python

import os, sys

text = str()
name = ""
line = ""

os.system("clear")

if len(sys.argv) > 1 :
    name = sys.argv[1]

    if os.path.isfile(sys.argv[1]) :
        with open(sys.argv[1], "r") as myfile :
            text = myfile.read()


while line != ":q" :
    os.system("clear")

    text = text.split("\n")
    i = 0    

    while i < len(text) - 1 :
        if i < 10 :
            print(str(i + 1) + " : " + text[i])

        else :
            print(str(i + 1) + ": " +text[i])

        i = i + 1

    myi = i + 1
    text = "\n".join(text)      

    if myi < 10 :
        line = raw_input(str(myi) + " > ")

    else :
        line = raw_input(str(myi) + "> ") 

    line = line.replace(":N", "\033[0m")
    line = line.replace(":Bl", "\033[5m")
    line = line.replace(":In", "\033[7m")
    line = line.replace(":B", "\033[1m")
    line = line.replace(":D", "\033[2m")
    line = line.replace(":I", "\033[3m")
    line = line.replace(":U", "\033[4m")

    line = line.replace(":fB", "\033[30m")
    line = line.replace(":fr", "\033[31m")
    line = line.replace(":fg", "\033[32m")
    line = line.replace(":fy", "\033[33m")
    line = line.replace(":fb", "\033[34m")
    line = line.replace(":fm", "\033[35m")
    line = line.replace(":fc", "\033[36m")
    line = line.replace(":flg", "\033[37m")

    line = line.replace(":flB", "\033[90m")
    line = line.replace(":flr", "\033[91m")
    line = line.replace(":flg", "\033[92m")
    line = line.replace(":fly", "\033[93m")
    line = line.replace(":flb", "\033[94m")
    line = line.replace(":flm", "\033[95m")
    line = line.replace(":flc", "\033[96m")
    line = line.replace(":fw", "\033[97m")

    line = line.replace(":bB", "\033[40m")
    line = line.replace(":br", "\033[41m")
    line = line.replace(":bg", "\033[42m")
    line = line.replace(":by", "\033[43m")
    line = line.replace(":bb", "\033[44m")
    line = line.replace(":bm", "\033[45m")
    line = line.replace(":bc", "\033[46m")
    line = line.replace(":blg", "\033[47m")

    line = line.replace(":blB", "\033[100m")
    line = line.replace(":blr", "\033[101m")
    line = line.replace(":blg", "\033[102m")
    line = line.replace(":bly", "\033[103m")
    line = line.replace(":blb", "\033[104m")
    line = line.replace(":blm", "\033[105m")
    line = line.replace(":blc", "\033[106m")
    line = line.replace(":bw", "\033[107m")

    sline = line.split(" ")

    if sline[0] == ":l" :
        text = text.split("\n")
        text[int(sline[1])-1] = sline[2].replace("_", " ")
        text = "\n".join(text)

    elif sline[0] == ":lw" :
        text = text.split("\n")
        text[int(sline[1])-1] = text[int(sline[1])-1].split(" ")
        text[int(sline[1])-1][int(sline[2])-1] = sline[3].replace("_", " ")
        text[int(sline[1])-1] = " ".join(text[int(sline[1])-1])
        text = "\n".join(text)

    elif line == ":q" :
        a = 1    

    else :
        text = text + line + "\n"

rep = raw_input("Save ? (Y/n) : ")

if rep == "n" :
    exit(0)

else :
    fname = raw_input("name : " + name + " ")

    if fname != "" :
        name = fname

    with open(name, "w") as myfile :
        myfile.write(text)


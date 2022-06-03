#########################Syntax Compiler##################################
'''
Author:Aniket Kumar
'''
import os


# This function will process the syntax of the source file


def compileCode(code):
    code2='#include "'+os.getcwd()+'/Modules/builtins.csq"\n'+code.replace("import", "#include").replace("main:", "int main(int argc, char const *argv[]){").replace("endmain", "return 0;}")
    return code2

# This function will read the process.cpp
def ReadProcess():
    # read process.cpp obj
    rp = open("process.cpp", 'r')
    # assigning code to code var
    code = compileCode(rp.read())
    return code

# This function will write process.cpp with new and compiled code


def writeProcess(code):
    # Write obj
    wp = open("process.cpp", 'w')
    # Writing
    wp.write(code)


# Driver code

if __name__ == "__main__":

    # Invoking readprocess and writeprocess
    writeProcess(ReadProcess())
    pass

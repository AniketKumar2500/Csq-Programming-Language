# Csq-Programming-Language
This is a programming language which is similar to C++ and C but its the next level version of C and C++ means it can give features which C and C++ can't.


# Why to use Csq?

* Easy Syntax
* Fast Runtime
* Having Libraries which can provide various supports
* Platform independent  (Executable haven't yet created for mac)


# Specialties

* Support OPPs
* Support dynamic typing by using var and def keyword for functions
* Allows to use C++ in Csq code

# Installation

* To install csq for linux you can download the directory LinuxSetup
* To install csq for windows you can download the directory WindowsSetup

# Simple Keywords
    def ->Used to define a function in which you don't have to put return type
    lam ->Using this you can create functions inside main
    func(name,args,code) ->Using this you can create functions in one line
    var -> Using this you can create variables in which you don't have to define it's type
    let -> Same as var
    _start_ ->Using this you can start a scope
    endhere ->Using this you can end a scope
    when -> This is same as if statement
    elif -> This is same as else if
    _if_ -> Same as when
    so -> Used after if condition and in _for_
    then -> Same as so but here you don't have to put stating curly brace
    forR(i,from,condition,steps) -> Loop for increment mode
    forAR(i,from,condition,steps) -> Loop for decrement mode
    forE(_var_,data) -> Element loop
    _for_ -> Same as for
    constructor(classname) -> Used to define a constructor
    _end_  -> Same as endhere
    __Cons__(classname) -> Same as constructor
    __init__(classname) -> Same as __Cons__
    inherit(classname) -> Used for inheritence
    as(from,to) -> This can create an alias of a datatype
    none -> \0
    vect(type,var_) -> Used to define vector
    Type(var) -> Returns type of the variables
# Execution

> Run csqEx executable file and now enter all the inputs asked by executable file.

# Examples 

## Hello World Program

> main: <br>
    &nbsp; print("Hello, World"); <br>
endmain

## Sum of array Program
:warning: ** The path of module may not be similar for you
>import "Modules/numcq.csq" <br>
>main: <br>
>&nbsp; array<int> ar; <br>
>&nbsp; ar.add(2,4,5,6); <br>
>&nbsp; print(ar.sum()); <br>
>endmain
  
## Program to find sum of two numbers using input
>main: <br>
>&nbsp; int a=input("Enter Number1:").toInt() <br>
>&nbsp; int b=input("Enter Number2:").toInt() <br>
>&nbsp; print("sum is:",a+b); <br>
>endmain
  
## Builtins Modules
* numcq.csq is a module which can be used in datascience and the simple and advance uses of array.
* builtins.csq is the core module which allows the basic and advance operations to performed.
* syntax.csq is the syntax module which is linked to compiler.
* Regex.csq is a module which can do operations releted to Regular expression.

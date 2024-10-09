#!/usr/bin/python3

import warnings
import os
import sys
import io

i = input("splash 1.0 -#$ ")
test = False


help = """
----SPLASH 1.0.b help pages----
when you start splash you get a prompt:

splash 1.0 -#$ 

at this prompt you enter commands or operations.
for example, say you want to add 2 + 2; you would then
enter the following at the shell prompt:

splash 1.0 -#$ 2 + 2

and when you press enter; you get this output:

splash 1.0 operation: add; output -# 4

and don`t worry! there are more math operands you can use.
such as:

splash 1.0 -#$ 2 + 2
splash 1.0 -#$ 2 - 2
splash 1.0 -#$ 2 * 2
splash 1.0 -#$ 2 / 2
and, last but not least,
splash 1.0 -#$ 2^2 

you can also use the `now` command in math operations!
the syntax and semantics  of this command are quite simple.
(please note ``now [number]^[number]`` is not allowed, nor is
''2^2 now [number] [operator] [number]``)
it works as follows:

splash 1.0 -#$ 2 + 2 now * 2
splash 1.0 operation: add; output -# 8

you get this output because 2 plus 2 equals 4, which multiplied by 2 equals 8.

And no terminal/shell would be complete without variables!
the basic syntax for defining a variable is as follows:

var [VARIABLE-NAME] = [VARIABLE-VALUE]

for example;

splash 1.0 -#$ var name = 'david goeke'
splash 1.0 -#$ print name
'david goeke'

splash 1.0 -#$ var number = 248
splash 1.0 -#$ print number
248

etc, etc.

"""

license = """
As of yet, there is no offical license for this project,
I may inculde it later.
"""

class Data:
    def __init__(self):
        self.variables = {}
    
    def read(self, id):
        return self.variables[id]
    
    def read_all(self):
        return self.variables
    
    def write(self, variable, value):
        variable_name = variable
        self.variables[variable_name] = value



variables = Data()



while True:
    
    # development option, i recommend you don`t use this. 
    if test:
        holder = []
        if "quit" in i:
            print("Goodbye!")
            break
        elif "exit" in i:
            print("Goodbye!")
            break
        for g in enumerate(i):
            holder.append(g)
        print(holder)
        i = input("splash 1.0 -#$ ")
        continue
        
    elif "quit" in i:
        print("Goodbye!")
        break
        
    elif "exit" in i:
        print("Goodbye!")
        break
        
    elif len(i) == 1:
        if str(i[0]) in variables.read_all():
            print(variables.read(i[0]))
            i = input("splash 1.0 -#$ ")
            continue
        print(i[0])
        i = input("splash 1.0 -#$ ")
        continue
                 
    elif i[0:4] == "var ":
        assign = i.find(' = ') 
        value = i[assign + 3:]
        if str(value) in variables.read_all():
            value = variables.read(value)
        else:
            if value.startswith("\'") and value.endswith("\'"):
                pass
            elif value.startswith("\"") and value.endswith("\""):
                pass
            elif value.startswith("[") and value.endswith("]"):
                value = list(value)
            elif value.startswith("{") and value.endswith("}"):
                print("dictionary's are not yet supported by splash 1.0.b.")
                i = input("splash 1.0 -#$ ")
                continue
                
            else:
                try:
                    value = int(value)
                except:
                    try:
                        value = float(value)
                    except:
                        print(f"error: {value} not a variable or number, and no matching quotation marks found")
                        del value
                        i = input("splash 1.0 -#$ ")
                        continue
        name = i[4:assign]
        variables.write(name, value)
        i = input("splash 1.0 -#$ ")
        continue
       
    elif "type" in i:
        t = i.index("type")
        if str(i[t + 5:]) in variables.read_all():
            value = variables.read(str(i[t + 5:]))
        else:
            value = i[t + 5:]
        print(type(value))
        i = input("splash 1.0 -#$ ")
        continue
       
    elif "license" in i:
        print(license)
        i = input("splash 1.0 -#$ ")
        continue

    elif " + " in i[0:10] != None:
        l = i.index(" + ")
        n = None
        num0 = i[:l]
        num1 = i[l + 3:]
        
        try:
            n = i.index(" now ")
        except:
            pass
            
        if n != None:
            num1 = i[l + 3:n]
        
        if str(num0) in variables.read_all():
            num0 = variables.read(num0)
        elif str(num1) in variables.read_all():
            num1 = variables.read(num1)

        try:
            try:
                num0 = int(num0)
            except:
                num0 = float(num0)
            
            try:
                num1 = int(num1)
            except:
                num1 = float(num1)
        except:
            print(f"{num0}, and/or {num1}, (or the values of the former,) are not int(s) or float(s). strign concatenation is not yet supported.")
            i = input("splash 1.0 -#$ ")
            continue
            
        if n != None:            
            rv = num0 + num1
            operand = i[n + 4:n + 7]
            if operand == " + ":
                try:
                    num = int(i[n + 7:n + 100000])
                except:
                    num = float(i[n + 7:n + 100000])
                rv = rv + num
            elif operand == " - ":
                try:
                    num = int(i[n + 7:n + 100000])
                except:
                    num = float(i[n + 7:n + 100000])
                rv = rv - num
            elif operand == " * ":
                try:
                    num = int(i[n + 7:n + 100000])
                except:
                    num = float(i[n + 7:n + 100000])
                rv = rv * num
            elif operand == " / ":
                try:
                    num = int(i[n + 7:n + 100000])
                except:
                    num = float(i[n + 7:n + 100000])
                rv = rv / num
            else:
                rv = num0 + num1
        else:
            rv = num0 + num1
        print(f"splash 1.0 operation: add; output: -# {rv}")
        
        i = input("splash 1.0 -#$ ")
        continue
        
    elif " - " in i[0:10] != None:
        l = i.index(" - ")
        n = None
        num0 = i[:l]
        num1 = i[l + 3:]
        
        try:
            n = i.index(" now ")
        except:
            pass
            
        if n != None:
            num1 = i[l + 3:n]
        
        if str(num0) in variables.read_all():
            num0 = variables.read(num0)
        elif str(num1) in variables.read_all():
            num1 = variables.read(num1)

        try:
            try:
                num0 = int(num0)
            except:
                num0 = float(num0)
            
            try:
                num1 = int(num1)
            except:
                num1 = float(num1)
        except:
            print(f"{num0}, and/or {num1}, (or the values of the former,) are not int(s) or float(s). \n strign concatenation is not yet supported.")
            i = input("splash 1.0 -#$ ")
            continue
            
        if n != None:            
            rv = num0 - num1
            operand = i[n + 4:n + 7]
            if operand == " + ":
                try:
                    num = int(i[n + 7:n + 100000])
                except:
                    num = float(i[n + 7:n + 100000])
                rv = rv + num
            elif operand == " - ":
                try:
                    num = int(i[n + 7:n + 100000])
                except:
                    num = float(i[n + 7:n + 100000])
                rv = rv - num
            elif operand == " * ":
                try:
                    num = int(i[n + 7:n + 100000])
                except:
                    num = float(i[n + 7:n + 100000])
                rv = rv * num
            elif operand == " / ":
                try:
                    num = int(i[n + 7:n + 100000])
                except:
                    num = float(i[n + 7:n + 100000])
                rv = rv / num
            else:
                rv = num0 - num1
        else:
            rv = num0 - num1
        print(f"splash 1.0 operation: subtract; output: -# {rv}")
        
        i = input("splash 1.0 -#$ ")
        continue
    
    elif " * " in i[0:10] != None:
        l = i.index(" * ")
        n = None
        num0 = i[:l]
        num1 = i[l + 3:]
        
        try:
            n = i.index(" now ")
        except:
            pass
            
        if n != None:
            num1 = i[l + 3:n]
        
        if str(num0) in variables.read_all():
            num0 = variables.read(num0)
        elif str(num1) in variables.read_all():
            num1 = variables.read(num1)

        try:
            try:
                num0 = int(num0)
            except:
                num0 = float(num0)
            
            try:
                num1 = int(num1)
            except:
                num1 = float(num1)
        except:
            print(f"{num0}, and/or {num1}, (or the values of the former,) are not int(s) or float(s). strign concatenation is not yet supported.")
            i = input("splash 1.0 -#$ ")
            continue
            
        if n != None:            
            rv = num0 * num1
            operand = i[n + 4:n + 7]
            if operand == " + ":
                try:
                    num = int(i[n + 7:n + 100000])
                except:
                    num = float(i[n + 7:n + 100000])
                rv = rv + num
            elif operand == " - ":
                try:
                    num = int(i[n + 7:n + 100000])
                except:
                    num = float(i[n + 7:n + 100000])
                rv = rv - num
            elif operand == " * ":
                try:
                    num = int(i[n + 7:n + 100000])
                except:
                    num = float(i[n + 7:n + 100000])
                rv = rv * num
            elif operand == " / ":
                try:
                    num = int(i[n + 7:n + 100000])
                except:
                    num = float(i[n + 7:n + 100000])
                rv = rv / num
            else:
                rv = num0 * num1
        else:
            rv = num0 * num1
        print(f"splash 1.0 operation: multiply; output: -# {rv}")
        
        i = input("splash 1.0 -#$ ")
        continue
        
    elif " / " in i[0:10] != None:
        l = i.index(" / ")
        n = None
        num0 = i[:l]
        num1 = i[l + 3:]
        
        try:
            n = i.index(" now ")
        except:
            pass
            
        if n != None:
            num1 = i[l + 3:n]
        
        if str(num0) in variables.read_all():
            num0 = variables.read(num0)
        elif str(num1) in variables.read_all():
            num1 = variables.read(num1)

        try:
            try:
                num0 = int(num0)
            except:
                num0 = float(num0)
            
            try:
                num1 = int(num1)
            except:
                num1 = float(num1)
        except:
            print(f"{num0}, and/or {num1}, (or the values of the former,) are not int(s) or float(s). strign concatenation is not yet supported.")
            i = input("splash 1.0 -#$ ")
            continue
            
        if n != None:            
            rv = num0 / num1
            operand = i[n + 4:n + 7]
            if operand == " + ":
                try:
                    num = int(i[n + 7:n + 100000])
                except:
                    num = float(i[n + 7:n + 100000])
                rv = rv + num
            elif operand == " - ":
                try:
                    num = int(i[n + 7:n + 100000])
                except:
                    num = float(i[n + 7:n + 100000])
                rv = rv - num
            elif operand == " * ":
                try:
                    num = int(i[n + 7:n + 100000])
                except:
                    num = float(i[n + 7:n + 100000])
                rv = rv * num
            elif operand == " / ":
                try:
                    num = int(i[n + 7:n + 100000])
                except:
                    num = float(i[n + 7:n + 100000])
                rv = rv / num
            else:
                rv = num0 / num1
        else:
            rv = num0 / num1
        print(f"splash 1.0 operation: divide; output: -# {rv}")
        
        i = input("splash 1.0 -#$ ")
        continue

    elif "^" in i:
        pow_s = i.index("^")
        num0 = i[:pow_s]
        num1 = i[pow_s+1:]

        try:
            try:
                num0 = int(num0)
            except:
                num0 = float(num0)
            
            try:
                num1 = int(num1)
            except:
                num1 = float(num1)
        except:
            print(f"{num0}, and/or {num1}, (or the values of the former,) are not int(s) or float(s). \n string concatenation is not yet supported.")
            i = input("splash 1.0 -#$ ")
            continue

        rv = pow(num0, num1)
        print(f"splash 1.0 operation: to-the-power-of; output: -# {rv}")
        i = input("splash 1.0 -#$ ")
        continue
        
    elif "help" in i:
        print(help)
        i = input("splash 1.0 -#$ ")
        continue
        
    elif "man" in i:
        print(help)
        i = input("splash 1.0 -#$ ")
        continue
        
    elif "print" in i:
        print_ = i.find("print")
        
            
        if str(i[print_ + 6:]) in variables.read_all():
            print(variables.read(str(i[print_ + 6:])))
            i = input("splash 1.0 -#$ ")
            continue
        else:
            pv = str(i[print_ + 6:])
            print(f"variable {pv} does not exist")
            i = input("splash 1.0 -#$ ")
            continue
            
    elif i[:] in variables.read_all():
        print(variables.read(str(i)))
        i = input("splash 1.0 -#$ ")
        continue
            
    elif i == "":
        i = input("splash 1.0 -#$ ")
        continue
        
    else:
        print("Unknown command, keyword, or operation.")
        i = input("splash 1.0 -#$ ")
        continue
        
        

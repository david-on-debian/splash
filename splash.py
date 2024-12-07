#!/usr/bin/python3


__version__ = '1.1.c'
version = '1.1'
name = "splash"

help_part1 = f"""
----{name.upper() + ' ' + __version__} help pages----
when you start splash you get a prompt:

{name + ' ' + version} -#$ 

at this prompt you enter commands or operations.
for example, say you want to add 2 + 2; you would then
enter the following at the shell prompt:

{name + ' ' + version} -#$ 2 + 2

and when you press enter; you get this output:

{name + ' ' + version} operation: add; output -# 4

and don`t worry! there are more math operands you can use.
such as:
"""
help_part2 = f""" 
{name + ' ' + version} -#$ 2 + 2
{name + ' ' + version} -#$ 2 - 2
{name + ' ' + version} -#$ 2 * 2
{name + ' ' + version} -#$ 2 / 2
and, last but not least,
{name + ' ' + version} -#$ 2 ^ 2 

you can also use the `now` command in math operations!
the syntax and semantics  of this command are quite simple.
it works as follows:

{name + ' ' + version} -#$ 2 + 2 now * 2
{name + ' ' + version} operation: add; output -# 8

you get this output because 2 plus 2 equals 4, which multiplied by 2 equals 8.

And no terminal/shell would be complete without variables!
the basic syntax for defining a variable is as follows:

var [VARIABLE-NAME] = [VARIABLE-VALUE]
"""
help_part3 = f"""
for example;

{name + ' ' + version} -#$ var name = 'david goeke'
{name + ' ' + version} -#$ print name
'david goeke'

{name + ' ' + version} -#$ var number = 248
{name + ' ' + version} -#$ print number
248

etc, etc.
"""

license = """
As of yet, there is no official license for this project,
I may include it later.
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

#def to_list(value):
#    value = list(value)
#    if value[0] == '[':
#        value.pop(0)
#    if value[value.__len__] == ']':
#        value.pop(value.__len__)
#    for char in value:
        
        


variables = Data()

test = False

while True:
    i = input(f"{name + ' ' + version} -#$ ")
        
    if "quit" in i:
        print("Goodbye!")
        break
        
    elif "exit" in i:
        print("Goodbye!")
        break
    
    elif len(i) == 1:
        if str(i[0]) in variables.read_all():
            print(variables.read(i[0]))
            continue
        print(i[0])
        continue
                 
    elif " == " in i:
        equals = i.index(" == ")
        first = i[:equals]
        last = i[equals + 4:]
        if first in variables.read_all():
            first = variables.read(first)
        if last in variables.read_all():
            last = variables.read(last)
        if first == last:
            print(f"{name + ' ' + version} boolean; output: -# True")
            continue
        else:
            print(f"{name + ' ' + version} boolean; output: -# False")
            continue

    elif " != " in i:
        equals = i.index(" != ")
        first = i[:equals]
        last = i[equals + 4:]
        if first in variables.read_all():
            first = variables.read(first)
        if last in variables.read_all():
            last = variables.read(last)
        if first != last:
            print(f"{name + ' ' + version} boolean; output: -# True")
            continue
        else:
            print(f"{name + ' ' + version} boolean; output: -# False")
            continue


    # these don`t work quite yet for some reason.
    #elif " < " in i:
    #    equals = i.index(" < ")
    #    first = i[:equals]
    #    last = i[equals + 4:]
    #    if first in variables.read_all():
    #        first = variables.read(first)
    #    if last in variables.read_all():
    #        last = variables.read(last)
    
    #    if first > last:
    #        print(f"{name + ' ' + version} boolean; output: -# True")
    #        continue
    #    else:
    #        print(f"{name + ' ' + version} boolean; output: -# False")
    #        continue

    #elif " > " in i:
    #    equals = i.index(" > ")
    #    first = i[:equals]
    #    last = i[equals + 4:]
    #    if first in variables.read_all():
    #        first = variables.read(first)
    #    if last in variables.read_all():
    #        last = variables.read(last)
    #    if first < last:
    #        print(f"{name + ' ' + version} boolean; output: -# True")
    #        continue
    #    else:
    #        print(f"{name + ' ' + version} boolean; output: -# False")
    #        continue

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
 #               value = to_list(value)
                value = list(value)
            elif value.startswith("{") and value.endswith("}"):
                print(f"dictionary's are not yet supported by {name + ' ' + version}.")
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
                        continue
        var_name = i[4:assign]
        variables.write(var_name, value)
        continue
       
    # A pseudo-developement option, feel free to tinker around with it.
    elif "type" in i:
        t = i.index("type")
        if str(i[t + 5:]) in variables.read_all():
            value = variables.read(str(i[t + 5:]))
        else:
            value = i[t + 5:]
        print(type(value))
        continue
       
    elif "license" in i:
        print(license)
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
            print(f"{num0}, and/or {num1}, (or the values of the former,) are not int(s) or float(s). string concatenation is not yet supported.")
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
            elif operand == " ^ ":
                try:
                    num = int(i[n + 7:])
                except:
                    num = float(i[n + 7:])
                rv = rv ** num
            else:
                rv = num0 + num1
        else:
            rv = num0 + num1
        print(f"{name + ' ' + version} operation: add; output: -# {rv}")
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
            print(f"{num0}, and/or {num1}, (or the values of the former,) are not int(s) or float(s). \n string concatenation is not yet supported.")
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
            elif operand == " ^ ":
                try:
                    num = int(i[n + 7:])
                except:
                    num = float(i[n + 7:])
                rv = rv ** num
            else:
                rv = num0 - num1
        else:
            rv = num0 - num1
        print(f"{name + ' ' + version} operation: subtract; output: -# {rv}")
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
            print(f"{num0}, and/or {num1}, (or the values of the former,) are not int(s) or float(s). string concatenation is not yet supported.")
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
            elif operand == " ^ ":
                try:
                    num = int(i[n + 7:])
                except:
                    num = float(i[n + 7:])
                rv = rv ** num
            else:
                rv = num0 * num1
        else:
            rv = num0 * num1
        print(f"{name + ' ' + version} operation: multiply; output: -# {rv}")
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
            print(f"{num0}, and/or {num1}, (or the values of the former,) are not int(s) or float(s). string concatenation is not yet supported.")
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
            elif operand == " ^ ":
                try:
                    num = int(i[n + 7:])
                except:
                    num = float(i[n + 7:])
                rv = rv ** num
            else:
                rv = num0 / num1
        else:
            rv = num0 / num1
        print(f"{name + ' ' + version} operation: divide; output: -# {rv}")
        continue

    elif " ^ " in i:
        l = i.index(" ^ ")
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
            print(f"{num0}, and/or {num1}, (or the values of the former,) are not int(s) or float(s). string concatenation is not yet supported.")
            continue
            
        if n != None:            
            rv = num0 ** num1
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
            elif operand == " ^ ":
                try:
                    num = int(i[n + 7:])
                except:
                    num = float(i[n + 7:])
                rv = rv ** num
            else:
                rv = num0 ** num1
        else:
            rv = num0 ** num1
        print(f"{name + ' ' + version} operation: exponent; output: -# {rv}")
        continue
        
    elif "help" in i:
        print(help_part1)
        c = input("Press Enter/Return To Continue: ")
        print(help_part2)
        c = input("Press Enter/Return To Continue: ")
        print(help_part3)
        continue
        
    elif "man" in i:
        print(help_part1)
        c = input("Press Enter/Return To Continue: ")
        print(help_part2)
        c = input("Press Enter/Return To Continue: ")
        print(help_part3)
        continue
        
    elif "print" in i:
        print_ = i.find("print")
              
        if str(i[print_ + 6:]) in variables.read_all():
            print(variables.read(str(i[print_ + 6:])))
            continue
        else:
            pv = str(i[print_ + 6:])
            print(f"variable {pv} does not exist")
            continue
            
    elif i[:] in variables.read_all():
        print(variables.read(str(i)))
        continue
            
    elif i == "":
        continue
        
    else:
        print("Unknown command, keyword, or operation.")
        continue

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
        continue

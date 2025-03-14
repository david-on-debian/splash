
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

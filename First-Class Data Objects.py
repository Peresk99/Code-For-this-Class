Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
abs
<built-in function abs>
import math
math.sqrt
<built-in function sqrt>

f = abs
f
<built-in function abs>
funcs = [abs, math.sqrt]
funcs
[<built-in function abs>, <built-in function sqrt>]
funcs[1](2)
1.4142135623730951
def example(functionArg, dataArg):
    return functionArg(dataArg)

example(abs, -4)
4

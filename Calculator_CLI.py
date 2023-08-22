import math
from colorama import Fore,Back,Style

def sum(x,y):
    print("The sum of the numbers is",(x + y))

def dif(x,y):
    print("The difference of the numbers is ",(x - y))

def mul(x,y):
    print("The product of the numbers is ",(x * y))

def div(x,y):
    print("The quotient when",x,"is divided by",y,"is",(x / y))

def logarithmic_e(x):
    print("Natural log of",x,"gives",math.log(x))

def logarithmic_10(x):
    print("Common log of",x,"gives",math.log10(x))

def power(x,y):
    print(x,"raised to the power",y,"gives",(math.pow(x,y)))

def percentage(x,y):
    print("The percent value of",x,"in",y,"is",(x/y)*100)

def sine(x):
    print("The sine of",x,"gives",math.sin(x))

def cosine(x):
    print("The cosine of",x,"gives",math.cos(x))

def tangent(x):
    print("The tangent of",x,"gives",math.tan(x))

def square_root(x):
    print("The square root of",x,"is",math.sqrt(x))

def find_factorial(x):
    print("The factorial of",x,"is",math.factorial(x))

def absolute(x):
    print("The absolute value of",x,"is",abs(x))


print(Fore.RED+"**** Scientific Calculator CLI ****"+Fore.RESET)
a = float(input(Fore.BLUE+"Enter first number : "+Fore.RESET))
ch = input(Fore.GREEN+"Enter your operator : "+Fore.RESET)

if(ch == "ln"):
    logarithmic_e(a)

elif(ch == "log10"):
    logarithmic_10(a)

elif(ch == "sin"):
    sine(a)

elif(ch == "cos"):
    cosine(a)

elif(ch == "tan"):
    tangent(a)

elif(ch == "sqrt"):
    square_root(a)

elif(ch == "fact"):
    find_factorial(a)

elif(ch == "abs"):
    absolute(a)
else:
    b = float(input(Fore.YELLOW+"Enter second number : "+Fore.RESET))

    if(ch == '+'):
        sum(a,b)

    elif(ch == '-'):
        dif(a,b)

    elif(ch == '*'):
        mul(a,b)

    elif(ch == '/'):
        div(a,b)
    
    elif(ch == '^'):
        power(a,b)

    elif(ch == '%'):
        percentage(a,b)
    
    else:
        print("***Invalid inputs***")
   
print(Fore.RED+"*** Program Ends ***"+Fore.RESET)
#A calculator App

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

import  math 
def sqrt(num):
    return math.sqrt(num)

def cos_function(num):
    return math.cos(num)

def sin_function(num):
    return math.sin(num)

def tan_function(num):
    return math.tan(num)

def modulus(num1, num2):
    return num1 % num2

def cube_root(num):
    return num ** (1/3)


def index(num):
    return num ** (index)


print (''' Please,  select the math operation:
   1 =  addition
   2 = subtraction
   3=  multiplication
   4 = division
   5 = square root
   6 = cosine
   7 = sine
   8 = tan
   9 = modulus
   10 = cube root
   11 = index ''')

#Take input from user
select = int(input("Select operations from 1,2,3,4,5,6,7,8,9,10:"))


#Enter parameters:
num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))
num =  int(input("Enter num"))
index =  int(input("Enter index"))    

if select == 1:
    print(num1, "+", num2, "=",
                    add(num1, num2))
  
elif select == 2:
    print(num1, "-", num2, "=",
                    subtract(num1, num2))
  
elif select == 3:
    print(num1, "*", num2, "=",
                    multiply(num1, num2))
  
elif select == 4:
    print(num1, "/", num2, "=",
                    divide(num1, num2))
elif select == 5:
    print("sqrt-num =",
                    sqrt(num))
elif select == 6:
    print(num, "=",
                   cosine(num))
elif select == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
elif select == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
elif select == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
elif select == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
elif select == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
                    



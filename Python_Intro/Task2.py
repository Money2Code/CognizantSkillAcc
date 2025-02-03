# Math Fun task3
def add(a, b):
   return a + b

def subtract(a, b):
   return a - b

def multiply(a, b):
    val=str(input( " Do you want to print table of a"))
    if val.lower() == "yes":
       for i in range(1,11):
          print(a, "*", i, "=", a * i)
    else:
       return a * b

def divide(a, b):
   if b == 0:
      return "Error! Division by zero"
   else:
      return a / b

a=int(input("Bro please enter the value of first number"))
b=int(input("Bro please enter the value of second number"))

print("Addition:The sum of a and b is", add(a, b))   
print("Subtraction:The sub of a and b is", subtract(a, b))
print("Multiplication:The multiplication of a and b is", multiply(a, b))
print("Division:The Division of a and b is", divide(a, b))

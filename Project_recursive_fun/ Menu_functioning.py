

import turtle

def factorial(num):
    if num < 0:
        print("Error: Factorial is not defined for negative numbers.")
    elif num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)
    

def fibonacci(num):
    if num <= 0:
        print("Error: Fibonacci sequence is not defined for negative numbers or non-integer values.")
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, num):
            a, b = b, a + b
        return b
    

hr=turtle.Turtle()
hr.left(90)
hr.speed(150)

def tree(i):
        if i<10:
            return
        else:
            hr.forward(i)
            hr.right(20)
            tree(i-10)
            hr.left(40)
            tree(i-10)
            hr.right(20)
            hr.backward(i)






def choice():
    print("Select the options")
    print("1. for Factorial")
    print("2. for Fibonacci")
    print("3. for Fractal patterns")
    print("4. for Exit")


    choice = int(input("Enter your choice: "))
    if choice == 1:
        num = int(input("Enter a number for factorial: "))
        val1=factorial(num)
        print(f"The factorial of {num} is {val1}")
    if choice == 2:
        num = int(input("Enter a number for Fibonacci: "))
        val2=fibonacci(num)
        print(f"The value of Fibonacci sequence is {val2}")

    if choice == 3:
        num = int(input("Enter a number for fractal"))
        tree(num)
        turtle.done()

    if choice == 4:
        print("Exiting...")
        exit()

choice()
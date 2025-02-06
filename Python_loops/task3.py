
    
def calculate_factorial(num):
        if num < 0:
            return "Error: Factorial is not defined for negative numbers."
        elif num == 0 or num == 1:
            return 1
        elif num == 1 and num == 2:
            return 2
        else:
            return num * calculate_factorial(num-1)
    

num = int(input("enter the number of factorial"))

value=calculate_factorial(num)
print(f"The factorial of {num} is {value}")

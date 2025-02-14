
import logging

logging.basicConfig(
    
    level=logging.INFO,
    filename='calculator.log',
    filemode='w',
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S'


)
def calculator():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
    try :
        if choice == 1:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 + num2
            print("The sum is", result)
            logging.info(f"The sum is, {result}")

   

        if choice == 2:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 - num2
            print("The difference is", result)
            logging.info(f"The difference is, {result}")
    
    

        if choice == 3:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 * num2
            print("The product is", result)
            logging.info(f"The product is { result}")


        if choice == 4:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if num2 == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
                logging.error("Division by zero attempted")
            result = num1 / num2
            print("The quotient is", result)
            logging.info(f"The quotient is {result}")
    
    except ValueError:
        print("Invalid input. Please enter a number.")
        logging.error("non-numeric value added")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        logging.error("Division by zero attempted")


calculator()
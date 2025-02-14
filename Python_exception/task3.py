def try_family():
    a= int(input("enter the first number "))
    b= int(input("enter the second number "))
    try :
        a/b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
    else:
        print("The result is", a/b)
    finally:
        print("This block will always execute")


try_family()
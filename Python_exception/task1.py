def exceptions():
    num=int(input("enter the number "))
    try :
        if num <1:
            raise ValueError("number should be positive")
        else:
            print("the number is positive")
        
        print(100/num)

    except ZeroDivisionError:
        print(" Oops! You cannot divide by zero")
        
    except ValueError as e:
        print("Invalid input! Please enter a valid number")


exceptions()
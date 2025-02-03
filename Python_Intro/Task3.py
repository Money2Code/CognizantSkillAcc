# lets check the positive and negative or zero


num = float(input('enter the number of to check '))

if num > 0:
    print(f'{num} This number is positive. Awesome!')
elif num < 0:
    print(f'{num} This number is negative. Better luck next time!')
    
else:
    print(f'{num} Zero it is. A perfect balance')
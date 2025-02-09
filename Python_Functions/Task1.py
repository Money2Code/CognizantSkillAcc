def greet_user(name):
    return f" hello  {name}! Welcome aboard"

def add_number(name,a,b):
    return greet_user(name)+f" the sum of {a} and {b}", a+b

print(add_number("John",5,7))
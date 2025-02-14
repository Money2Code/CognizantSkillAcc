def Type_of_exception():

    list1=[1,2,3,4,5,]
    dict1={"a":1, "b":2, "c":5}
    try:
        print(list1[6])
    except IndexError:
        print("Error: List index out of range")

    try:
        print(dict1["d"])
    except KeyError:
        print("Error: Key not found in the dictionary")
    
    try:
        5+"abc"
    except TypeError:
        print("Error: Unsupported operand type(s) for +: 'int' and 'str'")


Type_of_exception()

    
def make_sandwich(*ingredients):
    if ingredients:
        print("\check the ingredients")
        for ingredient in ingredients:
            print(ingredient)
    
make_sandwich("Chicken","Lettuce","tomato","Cheese")
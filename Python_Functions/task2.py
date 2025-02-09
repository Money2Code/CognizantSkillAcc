def describe_pet(pet_name,animal_type="dog"):
    return f"i have {animal_type} named {pet_name} "

print(describe_pet("bud"))
print(describe_pet("Max", "cat"))
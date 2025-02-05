import emoji

class eliglible():
    def __init__(self):
        self.name = input("enter Name please")
        self.age = int(input("enter Age please"))
    
    def check_eligible(self):
        if self.age < 0:
            return f"{self.name} Age cannot be negative. Please enter a positive number."
        elif self.age == 0:
            return f"{self.name} Age cannot be zero. Please enter a positive number."
        
        elif self.age >= 18:
            return f"{self.name} Congratulations! You are eligible to vote. Go make a difference! \U0001f600"
        else:
            X =18-self.age
            return f"{self.name} Oops! You’re not eligible yet. But hey, only {X} more years to go!" + (emoji.emojize(":zipper-mouth_face:"))
    

age_factor=eliglible()
results=age_factor.check_eligible()
print(results)
        
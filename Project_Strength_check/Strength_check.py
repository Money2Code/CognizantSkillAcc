class Strenth_check():

    def __init__(self, password):
        self.password = password

    def check_strength(self):
        count=0
        if len(self.password) < 8:
            print("Password should be at least 8 characters")

        if len(self.password) >=8:
            count+=2
            if not any(char.isupper() for char in self.password):
                print("Password should contain at least one uppercase letter")
            else:
                print("Password have at least one uppercase letter")
                count+=2
                if not any(char.islower() for char in self.password):
                    print("Password should contain at least one lowercase letter")
                else:
                    print("Password have at least one lowercase letter")
                    count+=2
                    if not any(char.isdigit() for char in self.password):
                        print("Password should contain at least one digit")
                    else:
                        print("Password have at least one digit")
                        count+=2
                        if not any(char in "!@#$%^&*()" for char in self.password):
                            print("Password donot contain at least one special character")
                        else:
                            print("Password have at least one special character")
                            count+=2

        return count

        
    
       
        


password=input("Please enter the strong password"+"\n")
obj1=Strenth_check(password)
val=obj1.check_strength()
print(f"the strength of your password on the scale of 10 is {val} ")
print(val)
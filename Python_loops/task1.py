class check_blast():

    def __init__(self,num):
        self.num = num
    def the_count(self):
        if self.num >0:
            while self.num > 0:
                print(self.num ,end=" ")
            
                self.num -= 1
            print("Blast off! 🚀")
        else:
            print("Error: Please enter a positive integer.")

num=int(input("Please enter a positive integer"))
obj1=check_blast(num)
obj1.the_count()

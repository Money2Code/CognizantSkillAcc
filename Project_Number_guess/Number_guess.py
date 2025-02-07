import random
number_to_guess = random.randint(1,100)

class Random():
    def __init__(self):
        self.number_to_guess = random.randint(1,100)
        print(self.number_to_guess)

    def guess_number(self, number):
        value=True
        count=0
        while True :
            if number == self.number_to_guess:
                print("Congratulations! You guessed the correct number.")
                break
            else :
                if number < self.number_to_guess:
                    print("Too low! Try again.")
                    number = int(input("Enter your guess: "))
                    count+=1
                else:
                    print("Too high! Try again.")
                    number = int(input("Enter your guess: "))
                    count+=1
            if count == 10:
                print("Sorry, you've run out of attempts. The correct number was", self.number_to_guess,"Better luck next time ")
                break
        return count
            

random_obj = Random()
user_input = int(input("Enter your guess: "))
count = random_obj.guess_number(user_input)
print("Number of attempts:", count)
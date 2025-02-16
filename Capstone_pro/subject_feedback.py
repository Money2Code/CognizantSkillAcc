class performance():
    def __init__(self):
        self.score={}

    def add_score(self, subject, score):
        try: 
            self.score[subject] = score
        except TypeError:
            print("Error: Score should be a number")

    def calculate_average(self):
      try :
         if self.score is not None:
             return sum(self.score.values()) / len(self.score)
         else:
             return 0
      except ZeroDivisionError:
         return "Error: No scores to calculate average"
    
    def minimum_score(self):
        try:
            if self.score is not None:
                return min(self.score.values())
            else:
                return "Error: No scores to find minimum"
        except ValueError:
            return "Error: No scores to find minimum"
    
    def maximum_score(self):
        try:
            if self.score is not None:
                return max(self.score.values())
            else:
                return "Error: No scores to find maximum"
        except ValueError:
            return "Error: No scores to find maximum"
        
    def display_result(self):
        print("\nStudent Performance Summary:")

        for subject,score in self.score.items():
            print(f"{subject}: {score}")

            print(f"Average Score: {self.calculate_average()}")
            print(f"Minimum Score: {self.minimum_score()}")
            print(f"Maximum Score: {self.maximum_score()}")
    

student = performance()
num_subjects= int(input("enter the number of subjects"))

for i in range(num_subjects):
    subject= input("Enter the subject name:")
    score=float(input("Enter the score for "+subject+": "))
    student.add_score(subject, score)


student.display_result()



class table():
    def __init__(self, num):
        self.num = num

    def print_table(self):
        if self.num >0:
            for i in range(1,11):
                print(f'{self.num} * {i} = {self.num * i}')


table_obj = table(int(input('Enter a number: ')))
table_obj.print_table()
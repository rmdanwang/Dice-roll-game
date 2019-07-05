# Final Exam by Ru Meng(Dan) Wang, contains Die Class
from random import randint

class Die:
    def __init__(self, number_sides):
        self.number_sides = number_sides

    def roll(self):
        return randint(1,self.number_sides)










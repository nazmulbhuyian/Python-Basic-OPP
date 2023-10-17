""" 
1. calculator class to do add, deduct, multiply, divide
2. Pen class. create three object with different instance attribute
3. Exam attend_to_exam get_marks 
 """


class Pen:
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color

pen1 = Pen('metador', 60, 'blue')
print(pen1.color, pen1.name, pen1.price)
pen2 = Pen('metador2', 50, 'red')
print(pen2.color, pen2.name, pen2.price)
pen3 = Pen('metador3', 40, 'black')
print(pen3.color, pen3.name, pen3.price)

from random import *

class Exam_attend:
    def __init__(self):
        random_marks = randint(70, 100)
        self.marks = random_marks
    
    def get_marks(self):
        print(f'You get marks {self.marks}')

nazmul = Exam_attend()
nazmul.get_marks()
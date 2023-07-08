import random
from pyscript import Element


students = ['Abdurrahim', 'Adamu', 'Alfonso', 'Alina', 'Asheer',
'Asri', 'Carl', 'Chidiebere', 'Chrizel', 'Colby', 'Comfort',
'Dany', 'Derrick', 'Diana', 'Dodou', 'Elizaveta', 'Emmanuel', 'Eric', 'Evan',
'Farhat', 'Geoffrey', 'Guilherme', 'Hani', 'Hibaq', 'Idris', 'Jazzmin', 'Jennifer',
'Jhonny', 'John', 'Joshua', 'Karyna', 'Kelvin', 'Kimberly', 'Larissa', 'Leangela',
'Linda', 'Luis', 'Marshal', 'Meng-Yun', 'Mohamed', 'Moises', 'Moreen',
'Muhanad', 'Muhydeen', 'Munawara', 'Neo R', 'Neo S', 'Olayemi', 'Oluwaseun', 'Paige',
'Precious', 'Quadri', 'Rachel', 'Rajib', 'Reem', 'Rita', 'Rukayat', 'Sarmad',
'Sergio', 'Shabana', 'Shaunyce', 'Shousuke', 'Soumaya', 'Stacy-Ann', 'Stanley',
'Swe', 'Thant', 'Tochukwu', 'Tran', 'Trevor', 'Uchenna', 'Victor F', 'Victor I',
'Wadzanayi', 'Yasser', 'Yonas', 'Yukina']

def pick(my_students):
    my_students.remove(student := random.choice(my_students))
    return student

def my_function():
    more = Element('test-input').value
    
    if more and more[0].lower() == 'n':
            students.clear()
    if students:
        winner = pick(students)
        display("And the winner is: " + winner + "!", target="helloDiv")
    else:
        display("No more students!", target="helloDiv")


my_function()
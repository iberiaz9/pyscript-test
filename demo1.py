import random
from pyscript import Element


students = ['Abdurrahim', 'Adamu', 'Alfonso',
'Asri', 'Carl', 'Chidiebere', 'Chrizel',
'Dany', 'Derrick', 'Diana', 'Dodou', 'Elizaveta',
'Farhat', 'Geoffrey', 'Guilherme', 'Hani', 'Hibaq',
'Jhonny', 'John', 'Joshua', 'Karyna', 'Kelvin',
'Linda', 'Luis', 'Marshal', 'Meng-Yun', 'Mohamed',
'Sergio', 'Shabana', 'Shaunyce', 'Shousuke',
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
import random
from pyscript import Element


students = ['Tomas','Sher','Sal','Jose','Ryan','Lawrence','Mel','Senay','Christie',
            'Vincent','Caitlyn','Adeline','Ray','Mike']

def pick(my_students):
    my_students.remove(student := random.choice(my_students))
    return student

def my_function():
    more = Element('test-input').value
    if more and more[0].lower() == 'n':
            students[:] = []
    if students:
        winner = pick(students)
        display("And the winner is: " + winner + "!", target="helloDiv")
    else:
        display("No more students!", target="helloDiv")
        

winner = pick(students)
display("And the winner is: " + winner + "!", target="helloDiv")
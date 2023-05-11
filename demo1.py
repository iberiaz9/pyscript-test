import random

students = ['Tomas','Sher','Sal','Jose','Ryan','Lawrence','Mel','Senay','Christie','Vincent','Caitlyn','Adeline','Ray','Mike']

def pick(my_students):
    my_students.remove(student := random.choice(my_students))
    return student

more = 'y'

while students and len(more) and not more[0] in 'nN':
    winner = pick(students)
    print("And the winner is: " + winner + "!")
    more = input("More? [y]/n: ")
    if not len(more):
        more = 'y'

print('Thanks for playing!')
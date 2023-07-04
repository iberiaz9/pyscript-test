import random
from pyscript import Element


students = [
"Osayma",
"Abdulrahman",
"Barnabas",
"Muhammed",
"Fatma",
"Elijah",
"Abdulaziz",
"Georgios",
"Myung",
"Rhett",
"Mahmoud",
"Sara",
"Tshepo",
"Muhammad",
"Trae",
"Obinna",
"Spencer",
"Gerhard",
"Judith",
"Ahmad",
"Melanie",
"Saron",
"Nathan",
"Ashtin",
"Bunnita",
"Thi"
]

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
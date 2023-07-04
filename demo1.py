import random
from pyscript import Element


students = [
'Idris Abdullahi',
'Rukayat Adegboyega',
'Muhydeen Akinleye',
'Yasser Alotibi',
'Stanley Ameh',
'Yonas Asmelash Nuguse',
'Stacy-Ann Bryan',
'Jhonny Campos',
'Sergio Coelho Jr',
'Paige Doering',
'Chrizel Du Plooy',
'Derrick Edward',
'Victor Fidelis',
'Evan Graven',
'Thant Zaw Htet',
'Soumaya Abdraman Ibrahim Mahamat',
'Abdurrahim Isah',
'Colby Junior Kapondo',
'Marcia Keesling',
'Asheer Khubchandani',
'Wadzanayi Kuweta',
'Baraa Lazkani',
'Mohamed Bishar Maalim',
'Elizaveta Medvedeva',
'Abdulaziz Mohammed',
'Marshal Mutisi',
'Linda Niiwo',
'Chidiebere Obioha',
'Buthaina Orabi',
'Moises Preciado',
'Neo Radithobane',
'Rajib Rai',
'Shaunyce Rogers',
'Neo Sahadeo',
'Shabana Shaik',
'John Slavinskas',
'Jazzmin Smith',
'Oluwaseun Sosami',
'Geoffrey Wahabunwa',
'Luis Zegarra',
'Hibaq Adam',
'Joshua Adeniji',
'Diana Ahmadi',
'Hani Almaleh',
'Reem Almasri',
'Uchenna Anya',
'Guilherme Araujo',
'Munawara Ayubi',
'Meng-Yun Chen',
'Alina Diaz',
'Trevor Do',
'Rachel Erickson',
'Kelvin Fordjour',
'Dany Garcia Delgado',
'Alfonso Gutierrez',
'Muhanad Haider',
'Farhat Hamraz',
'Victor Ifatokun',
'Sarmad Khalid',
'Tran Thuy Dung Le',
'Larissa Lima',
'Jennifer Lord',
'Shousuke Motomura',
'Precious Mozia',
'Moreen Mucunguzi',
'Quadri Muhammed',
'Eric Ndungu',
'Adamu Nuradeen',
'Emmanuel Okoh',
'Olayemi Olayiwola',
'Tochukwu Onunze',
'Swe Zin Ya Min Oo',
'Kimberly Pineda',
'Comfort Progress',
'Karyna Reut',
'Dodou Sanyang',
'Asri Soleyn',
'Carl Thornton',
'Rita Ukwome',
'Leangela Wynn',
'Yukina Yoshida'
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
import random

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

number = ['0','1','2','3','4','5','6','7','8','9']

simbolos = ['!','@','#','$','%','¨','&','*','(',')','-','=','+','{','}','[',']',';',':','<','>','.','?','/','|']

print("Welcome to the Password Manager!")

nr_letter = int(input("How many letters would you like in your password?\n"))

nr_number = int(input("How many numbers would you like in your password?\n"))
nr_simbolos = int(input("How many simbols would you like in your password?\n"))

password = ''

for i in range(nr_letter):
    password += random.choice(alfabeto)

for i in range(nr_number):
    password += random.choice(number)   

for i in range(nr_simbolos):
    password += random.choice(simbolos)

print("Your password is:", password)
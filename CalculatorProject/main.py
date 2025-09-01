
print(" Calculator Project \n")

def sum(num1, num2):
    return print(f"{num1 + num2}")

def subtraction(num1, num2):
    return print(f"{num1 - num2}")

def division(num1, num2):
    return print(f"{num1 / num2}")

def Moltiply(num1, num2):
    return print(f"{num1 * num2}")

def Modulo(num1, num2):
    return print(f"{num1 % num2}")

while True:
    print("Choose Operation: \n")
    choose = int(input("-1 Sum \n-2 Subtraction \n-3 Division \n-4 Moltiply \n-5 Modulo \n "))
    num1 = int(input("Choose First Number: \n"))
    num2 = int(input("Choose Second Number: \n"))
    if (choose == 1):
        sum(num1, num2)
    if (choose == 2):
        subtraction(num1, num2)
    if (choose == 3):
        division(num1, num2)
    if (choose == 4):
        Moltiply(num1, num2)
    if (choose == 5):
        Modulo(num1, num2)
    continua = str(input("Do you want continue? Type 'yes' or 'no' ")).lower()
    if continua == 'no':
        break
    else:
        continue
    
    











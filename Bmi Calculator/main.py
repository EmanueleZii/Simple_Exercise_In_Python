print("Welcome to BMI Calculator")
height = float(input("Give me your height"))
weight = float(input("Give me your weight"))

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight / 1.65 ** 2

'''
<16.00  Grave magrezza
16.00 - 16.99 Visibilmente sottopeso
17.00 - 18.49 Leggermente sottopeso
18.50 - 24.99 Peso ideale
25.00 - 29.99 Sovrappeso
30.00 - 34.99 Obesità di I classe
35.00 - 40.00 Obesità di II classe
>40.00 Obesità di III classe
'''
print(bmi)
if bmi<16.00:
    print("Grave magrezza")
if bmi>=16.00 and bmi <= 16.99:
    print("Visibilmente sottopeso")
if bmi>=17.00 and bmi <= 18.49:
    print("Leggermente sottopeso")
if bmi>=18.50 and bmi <= 24.99:
    print("Peso ideale")
if bmi>=25.00 and bmi <= 29.99:
    print("Sovrappeso")
if bmi>=30.00 and bmi <= 34.99:
    print("Obesità di I classe")
if bmi>=35.00 and bmi <= 40.00:
    print("Obesità di II classe")
if bmi>=40.00:
    print("Obesità di III classe")
















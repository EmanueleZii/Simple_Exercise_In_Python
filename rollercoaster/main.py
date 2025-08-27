
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
bill = 0
if height>=120:

    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))

    if age <=12:
        print("Please pay $5.")
        bill += 5
    elif age <= 18:
        print("Please pay $7.")
        bill += 7
    elif age<22:
        print("Please pay $9.")
        bill += 9
    else:
        print("Please pay $12.")
        bill += 12
    photo = input("Do you want a photo taken? Y or N. ")

    if photo == "Y":
        print("Please pay an extra $3.")
        bill += 3
    else:
        print("No photo will be taken.")
    print(f"Your final bill is ${bill}. Enjoy the ride!")
else:
    print("Sorry you have to grow taller before you can ride")

















import random

fruit = ["apple", "banana", "cherry", "date"]

state =["Lazio", "Milano", "Reggio Calabria" ]

state[1] = "Sicilia"
 
def main():
    print(random.choice(fruit))
    print(state[1])

    for f in fruit:
        print(f)

if __name__ == "__main__":
    main()

dict = {}

print("Welcome To Bid of chairity")

while True:
    nameofBidders = input("What's your name ? \n ")
    bid = int(input("How Much is you Bid ? \n "))

    dict[nameofBidders] = bid

    print(f"Name of bidders: {nameofBidders}")
    print(f"bid: {dict[nameofBidders]}")
    continua = str(input("Are there any other bidders? Type 'yes' or 'no' \n")).lower()
    if continua == 'yes':
       continue
    elif continua == 'no':
        break

# Alla fine mostra chi ha offerto di più
winner = max(dict, key=dict.get)
print(f"\nThe winner is {winner} with a bid of {dict[winner]}!")


























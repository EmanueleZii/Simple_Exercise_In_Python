#import random

arr = [1,2,3,44,77,100,56,89,98,45,109,234,456,567]

def max(arr):
    max = 0
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

def main():
    print("Il valore massimo è:", max(arr))

if __name__ == "__main__":
    main()

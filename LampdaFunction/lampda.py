square = lambda x: x**2
result = square(5)
print(result) # Output: 25

# Example of using lambda with filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(", ".join(map(str, even_numbers))) # Output: 2, 4, 6, 8, 10





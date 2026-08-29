def calculate_square(number):
    square = number**2
    return square


number = float(input("Enter a number: "))
result = calculate_square(number)
print("Square = ", result)

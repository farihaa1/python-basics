#numbers = [12, 7, 18, 25, 30, 41, 56, 63]
#numbers = [-10, 7, -2, 15, 20, -9, 30]


numbers = [3, 3, 3, 3]


even_count = 0
odd_count = 0

even_sum = 0
odd_sum = 0

largest_even = None
largest_odd = None

for number in numbers:

    if number % 2 == 0:
        even_count += 1
        even_sum += number
        if largest_even is None:
            largest_even = number
        elif number > largest_even:
            largest_even = number

    else:
        odd_count += 1
        odd_sum += number
        if largest_odd is None:
            largest_odd = number
        elif number > largest_odd:
            largest_odd = number


print("Even count:", even_count)
print("Odd count:", odd_count)
print("Even sum:", even_sum)
print("Odd sum:", odd_sum)
print("Largest even:", largest_even)
print("Largest odd:", largest_odd)


# Create a list containing x for every x in numbers where x is even.
even = [x for x in numbers if x % 2 == 0]
odd = [x for x in numbers if x % 2 != 0]

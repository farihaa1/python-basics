numbers = [10, 20, 30, 40, 50]

result = []

for i in range(len(numbers)-1, -1, -1):

    # append() adds one element to the end of a list.
    result.append(numbers[i])

print(result)

result = list(reversed(numbers))
print(result)

#slicing
# list[start:stop:step]
result = numbers[::-1]  # creates a new sequence.
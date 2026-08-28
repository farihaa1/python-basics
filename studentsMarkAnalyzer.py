marks = [75, 66, 22, 82, 91, 64, 88, 55, 33]

total = 0
highest = marks[0]
lowest = marks[0]
passed = 0
failed = 0

for mark in marks:
    total += mark

    if mark > highest:
        highest = mark
    if mark < lowest:
        lowest = mark
    if mark >= 40:
        passed += 1
    else:
        failed += 1

average = total/len(marks)
# len() returns the number of elements

print("Total: ", total)
print("average: ", average)
print("highest: ", highest)
print("lowest: ", lowest)
print("passed: ", passed)
print("failed: ", failed)

total = sum(marks)
average = total/len(marks)
highest = max(marks)
lowest = min(marks)

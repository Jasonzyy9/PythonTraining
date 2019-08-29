'''numbers = [3, 4, 10, 16, 12]
for count1 in numbers:
    maxnum = count1
    for count2 in numbers:
        if count2 > max:
            maxnum = count2
print(maxnum)'''

numbers = [3, 4, 10, 16, 12]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

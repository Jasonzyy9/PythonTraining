'''numbers = [5, 2, 1, 5, 7, 4, 1, 5]
numbers2 = numbers.copy()
for number1 in range(len(numbers)):
    count = numbers[number1]
    for number2 in numbers[number1+1:len(numbers)]:
        if count == number2:
            numbers2.remove(count)
print(numbers2)
This is a wrong method!'''

numbers = [5, 2, 1, 5, 7, 4, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
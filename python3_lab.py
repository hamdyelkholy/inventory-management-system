import math

# Task 01
def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"
    for char in text:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Python Programming"))
# Output:
# 2


# Task 02
def find_char_locations(text):
    positions = []
    for i in range(len(text)):
        if text[i].lower() == "i":
            positions.append(i)
    return positions

print(find_char_locations("iti summer training"))
# Output:
# [0, 2, 7, 13, 16]


# Task 03
def first_and_last(text):
    if len(text) == 1:
        return text
    return text[0] + text[-1]

print(first_and_last("Python"))
print(first_and_last("A"))
# Output:
# Pn
# A


# Task 04
def sort_numbers(numbers):
    numbers.sort()
    print("Ascending:", numbers)
    numbers.sort(reverse=True)
    print("Descending:", numbers)

numbers = [15, 3, 42, 8, 23]
sort_numbers(numbers)
# Output:
# Ascending: [3, 8, 15, 23, 42]
# Descending: [42, 23, 15, 8, 3]


# Task 05
def remove_duplicates(numbers):
    new_list = []
    removed = 0
    for item in numbers:
        if item in new_list:
            removed += 1
        else:
            new_list.append(item)
    return new_list, removed

print(remove_duplicates([1, 2, 3, 2, 4, 1, 5]))
# Output:
# ([1, 2, 3, 4, 5], 2)


# Task 06
def transform_numbers(numbers):
    result = [i**2 if i % 2 != 0 else i / 2 for i in numbers]
    return result

print(transform_numbers([1, 2, 3, 4, 5]))
# Output:
# [1, 1.0, 9, 2.0, 25]


# Task 07
def analyze_tuple(tup, item):
    count = 0
    positions = ()
    for i in range(len(tup)):
        if tup[i] == item:
            count += 1
            positions += (i,)
    return count, positions

count, positions = analyze_tuple((1, 2, 3, 2, 4, 2, 5), 2)
print("Count:", count)
print("Positions:", positions)
# Output:
# Count: 3
# Positions: (1, 3, 5)


# Task 08
def unpack_and_sum(tup):
    first, *middle, last = tup
    middle_sum = sum(middle)
    return first, last, middle_sum

first, last, middle_sum = unpack_and_sum((10, 20, 30, 40, 50))
print("First:", first)
print("Last:", last)
print("Middle sum:", middle_sum)
# Output:
# First: 10
# Last: 50
# Middle sum: 90


# Task 09
def lists_to_dict(keys, values):
    d = {}
    for i in range(len(keys)):
        d[keys[i]] = values[i]
    return d

print(lists_to_dict(['name', 'age', 'city'], ['Ali', 25, 'Cairo']))
# Output:
# {'name': 'Ali', 'age': 25, 'city': 'Cairo'}


# Task 10
def filter_and_inflate(products):
    new_dict = {}
    for key, value in products.items():
        if value > 50:
            new_dict[key] = value * 1.10
    return new_dict

print(filter_and_inflate({
    'apple': 30,
    'banana': 60,
    'orange': 80
}))
# Output:
# {'banana': 66.0, 'orange': 88.0}


# Task 11
def find_palindromes(words):
    result = set()
    for word in words:
        if word == word[::-1]:
            result.add(word)
    return result

print(find_palindromes([
    'level',
    'hello',
    'radar',
    'world',
    'civic'
]))
# Output:
# {'level', 'civic', 'radar'}


# Task 12
def check_coordinate(f_set, point):
    return point in f_set

f_set = frozenset([(1, 2), (3, 4), (5, 6)])

print(check_coordinate(f_set, (3, 4)))
print(check_coordinate(f_set, (7, 8)))
# Output:
# True
# False

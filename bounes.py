
# Task B1
def invert_dict(d):
    new_d = {}
    for key, val in d.items():
        new_d[val] = key
    return new_d

print(invert_dict({'a': 1, 'b': 2, 'c': 1}))
# Output: {1: 'c', 2: 'b'}


# Task B2
def even_products(l1, l2):
    return [a * b for a, b in zip(l1, l2) if a % 2 == 0 and b % 2 == 0]

print(even_products([2, 3, 4, 6], [4, 5, 2, 3]))
# Output: [8, 8]


# Task B3
def rotate_right(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]

print(rotate_right([1, 2, 3, 4, 5], 2))
# Output: [4, 5, 1, 2, 3]


# Task B4
import math

def factorial_tuples(n):
    return [(i, math.factorial(i)) for i in range(1, n + 1)]

print(factorial_tuples(5))
# Output: [(1, 1), (2, 2), (3, 6), (4, 24), (5, 120)]


# Task B5
def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0
    for x in num_set:
        if (x - 1) not in num_set:
            y = x + 1
            while y in num_set:
                y += 1
            longest = max(longest, y - x)
    return longest

print(longest_consecutive([100, 4, 200, 1, 3, 2]))
# Output: 4


# Task B6
def check_tic_tac_toe(board):
    lines = []
    lines.extend(board)
    for col in range(3):
        lines.append([board[row][col] for row in range(3)])
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])

    for line in lines:
        if line[0] == line[1] == line[2] and line[0] in ['X', 'O']:
            return f"{line[0]} wins"
    return "No winner"

print(check_tic_tac_toe([['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'X']]))
# Output: X wins


# Task B7
def most_frequent_char(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    
    max_char = s[0]
    max_count = 0
    for char, count in counts.items():
        if count > max_count:
            max_count = count
            max_char = char
    return max_char

print(most_frequent_char('programming'))
# Output: g


# Task B8
def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

print(reverse_sentence('Hello World from Python'))
# Output: Python from World Hello


# Task B9
def caesar_cipher(text, shift=3):
    result = []
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result.append(chr((ord(c) - base + shift) % 26 + base))
        else:
            result.append(c)
    return "".join(result)

print(caesar_cipher('Hello'))
print(caesar_cipher('Python 3.10!'))
# Output:
# Khoor
# Sbwkrq 3.10!
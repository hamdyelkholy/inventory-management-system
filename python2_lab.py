# Task 1
def calculate_price(item_name: str, price: float, tax_rate: float = 0.14, discount: float = 0.0):
    finalPrice = (price - discount) * (1 + tax_rate)
    return finalPrice

print(calculate_price('Mouse', 100.0))
print(calculate_price('Keyboard', 200.0, discount=20.0))


# Task 2
def summarize_event(event_name: str, *attendees: str, **metadata):
    print(f"Event: {event_name} ({len(attendees)} Attendees)")
    
    attendee = ""
    for name in attendees:
        if attendee == "":
            attendee = name
        else:
            attendee += ", " + name
    print(f"Attendees: {attendee}")

    details = ""
    for key, value in metadata.items():
        if details == "":
            details = f"{key}: {value}"
        else:
            details += f" | {key}: {value}"
    print(f"Details: {details}")

summarize_event('Python Lab', 'Ali', 'Sara', 'Omar', room='Lab 3', date='Today')


# Task 3
get_cube = lambda x : x ** 3
full_name = lambda first, last : f'{first} {last}'
is_adult = lambda age: True if age >= 18 else False

print(get_cube(3))
print(full_name('Ahmed', 'Hassan'))
print(is_adult(20))


# Task 4
def sum_range(n):
    if n == 1:
        return 1
    else:
        return n + sum_range(n - 1)

print(sum_range(5))
print(sum_range(10))


# Task 5
def transform_list(numbers, operation):
    result = []
    for item in numbers:
        result.append(operation(item))
    return result

def square(x):
    return x ** 2

print(transform_list([1, 2, 3, 4], square))
print(transform_list([1, 2, 3, 4], lambda x: x * 10))


# Task 6
def make_formatter(prefix: str):
    def format_message(message: str):
        return f'[{prefix}] {message}'
    return format_message

info_log = make_formatter('INFO')
error_log = make_formatter('ERROR')

print(info_log('Server started successfully'))
print(error_log('Connection failed'))
# ==========================================================
# Python Lab 1
# Complete Solution - AI Assisted
# ==========================================================


# ==========================================================
# Task 01: Student Assessment Tool
# Concepts:
# input().split(), multiple assignment, swapping,
# print() formatting, type casting and del
# ==========================================================

print("\n========== TASK 01 ==========")

# Read two student names from one line
name1, name2 = input("Enter two names: ").split()

# Assign both scores at the same time
score1, score2 = 85.5, 92.0

# Swap names and scores without using a third variable
name1, name2 = name2, name1
score1, score2 = score2, score1

# Display the student record
print(
    "[RECORD]",
    name1,
    score1,
    name2,
    score2,
    sep=" ::: ",
    end="\n--- FINISHED RECORD ---\n"
)

# Calculate total score and convert it to integer and string
combined_score = int(score1 + score2)
combined_score_string = str(combined_score)

print(
    "Total Score (Int):",
    combined_score,
    "| Total Score (Type):",
    type(combined_score_string)
)

# Delete the temporary calculation
del combined_score


# ==========================================================
# Task 02: Online Retail Shipping
# Concepts:
# logical operators, membership operator and ternary operator
# ==========================================================

print("\n========== TASK 02 ==========")

amount = float(input("Amount = "))
country = input("Country = ").lower()

# Countries included in the duty-free zone
duty_free_countries = [
    "egypt",
    "uae",
    "saudi",
    "kuwait"
]

# Check if the order qualifies for free shipping
eligible = (
    amount >= 500.0
    and country in duty_free_countries
)

# Ternary operator for shipping status
shipping_status = (
    "Free Express Shipping"
    if eligible
    else "Standard Shipping (50 EGP)"
)

# Identity check as requested in the lab
vip_flag = shipping_status is "Free Express Shipping"

print(
    "Delivery:",
    shipping_status,
    "| VIP Logistics Flag:",
    vip_flag
)


# ==========================================================
# Task 03: Electricity Billing Calculator
# Concepts:
# nested conditionals, validation and calculations
# ==========================================================

print("\n========== TASK 03 ==========")

units = float(input("Units = "))
account_type = input("Type = ").lower()

# Validate the input values
if units < 0:
    print("Error: Units cannot be negative")

elif account_type not in ["res", "com"]:
    print("Error: Unknown account type")

else:

    # Calculate the base bill according to consumption tiers
    if units <= 100:
        base_bill = units * 0.75

    elif units <= 250:
        base_bill = (
            (100 * 0.75)
            + ((units - 100) * 1.20)
        )

    else:
        base_bill = (
            (100 * 0.75)
            + (150 * 1.20)
            + ((units - 250) * 1.80)
        )

    # Apply the correct account tax
    if account_type == "res":

        tax = base_bill * 0.05
        total_due = base_bill + tax

    else:

        tax = base_bill * 0.12
        total_due = base_bill + tax + 20

    print(
        f"Base Bill: {base_bill:.2f} EGP | "
        f"Tax: {tax:.2f} EGP | "
        f"Total Due: {total_due:.2f} EGP"
    )


# ==========================================================
# Task 04: Network Response Interpreter
# Concepts:
# Python 3.10+ match-case pattern matching
# ==========================================================

print("\n========== TASK 04 ==========")

status_code = int(input("Enter status code: "))

match status_code:

    case 200 | 201:
        message = (
            "SUCCESS: Request fulfilled "
            "and resource ready."
        )

    case 400 | 422:
        message = (
            "CLIENT ERROR: Bad request "
            "or unprocessable payload."
        )

    case 401 | 403:
        message = (
            "ACCESS DENIED: Authentication "
            "required or forbidden."
        )

    case 404:
        message = (
            "NOT FOUND: The requested "
            "resource does not exist."
        )

    case 500 | 502 | 503:
        message = (
            "SERVER ERROR: Upstream server "
            "is unavailable."
        )

    case _:
        message = (
            "UNKNOWN CODE: Protocol response "
            "code unmapped."
        )

print(f"[Response {status_code}] {message}")


# ==========================================================
# Task 05: Range, Break and Continue
# Concepts:
# range() with step, continue and break
# ==========================================================

print("\n========== TASK 05 ==========")

start = int(input("Start = "))
stop = int(input("Stop = "))
step = int(input("Step = "))

for number in range(start, stop, step):

    # Stop the loop if the number is greater than 80
    if number > 80:
        break

    # Skip numbers divisible by 3
    # or numbers ending with digit 5
    if number % 3 == 0 or number % 10 == 5:
        continue

    print(number, end=" # ")

print("[SCAN COMPLETE]")


# ==========================================================
# Task 06: Coordinate Grid
# Concepts:
# nested for loops and row/column conditions
# ==========================================================

print("\n========== TASK 06 ==========")

n = int(input("N = "))

for i in range(1, n + 1):

    for j in range(1, n + 1):

        # Main diagonal
        if i == j:
            print("[X]", end=" ")

        # Other cells display their coordinates
        else:
            print(f"({i},{j})", end=" ")

    # Move to the next row
    print()


# ==========================================================
# Task 07: Warehouse Stock Manager
# Concepts:
# while True, sentinel value, validation and counters
# ==========================================================

print("\n========== TASK 07 ==========")

# Initial stock
stock = 50

# Counters
restocks = 0
dispatches = 0

while True:

    adjustment = int(
        input(
            "Stock adjustment "
            "(+received / -dispatched / 0=finish): "
        )
    )

    # Zero means finish
    if adjustment == 0:
        break

    # Positive number means new stock received
    if adjustment > 0:

        stock += adjustment
        restocks += 1

    # Negative number means stock dispatched
    else:

        quantity = -adjustment

        # Reject dispatch if there is not enough stock
        if quantity > stock:

            print(
                "Dispatch Rejected: "
                "Insufficient inventory"
            )

        else:

            stock -= quantity
            dispatches += 1

            # Display warning when stock becomes zero
            if stock == 0:
                print("Warning: Stock Depleted!")


# Final inventory report
print(
    "[INVENTORY FINAL REPORT] "
    f"Current Units: {stock} | "
    f"Restocks: {restocks} | "
    f"Dispatches: {dispatches}"
)


# ==========================================================
# BONUS: Cinema Ticket & Snack Checkout
# Concepts:
# while loop, match-case, multiple input,
# calculations, ternary operator and type casting
# ==========================================================

print("\n========== BONUS ==========")

# Cinema prices
prices = {
    1: 80,
    2: 130,
    3: 200,
    4: 45,
    5: 25
}

# Item names
items = {
    1: "Standard 2D Ticket",
    2: "IMAX 3D Ticket",
    3: "VIP Recliner Ticket",
    4: "Popcorn Combo",
    5: "Soda Beverage"
}

# Store selected items
cart = []

# Start total
total_bill = 0.0


# ------------------------------
# Booking Menu
# ------------------------------

while True:

    print("\n----- CINEMA MENU -----")
    print("(1) Standard 2D Ticket - 80 EGP")
    print("(2) IMAX 3D Ticket - 130 EGP")
    print("(3) VIP Recliner Ticket - 200 EGP")
    print("(4) Popcorn Combo - 45 EGP")
    print("(5) Soda Beverage - 25 EGP")
    print("(0) Proceed to Payment")

    choice, quantity = map(
        int,
        input("Enter item number and quantity: ").split()
    )

    # Finish selecting items
    if choice == 0:
        break

    # Select price using match-case
    match choice:

        case 1:
            price = 80

        case 2:
            price = 130

        case 3:
            price = 200

        case 4:
            price = 45

        case 5:
            price = 25

        case _:
            print("Invalid item!")
            continue

    # Calculate item subtotal
    subtotal = price * quantity

    # Add to total
    total_bill += subtotal

    # Save item information
    cart.append(
        (
            items[choice],
            quantity,
            price,
            subtotal
        )
    )

    print(
        f"Added: {items[choice]} x {quantity} "
        f"= {subtotal:.2f} EGP"
    )


# ------------------------------
# Apply Loyalty Discount
# ------------------------------

discount = (
    total_bill * 0.10
    if total_bill > 250
    else 0
)

final_bill = total_bill - discount


# ------------------------------
# Payment
# ------------------------------

print("\n========== CHECKOUT ==========")

print(f"Subtotal: {total_bill:.2f} EGP")
print(f"Discount: {discount:.2f} EGP")
print(f"Final Bill: {final_bill:.2f} EGP")

# Continue asking until payment is enough
while True:

    cash = float(input("Cash tendered: "))

    if cash >= final_bill:
        break

    print("Insufficient payment. Please pay more.")


# Calculate change
change = cash - final_bill


# ------------------------------
# Final Itemized Summary
# ------------------------------

print("\n========== FINAL SUMMARY ==========")

for item_name, quantity, price, subtotal in cart:

    print(
        f"{item_name} | "
        f"Qty: {quantity} | "
        f"Price: {price:.2f} EGP | "
        f"Subtotal: {subtotal:.2f} EGP"
    )

print("-----------------------------------")
print(f"Subtotal: {total_bill:.2f} EGP")
print(f"Discount: {discount:.2f} EGP")
print(f"Final Bill: {final_bill:.2f} EGP")
print(f"Paid: {cash:.2f} EGP")
print(f"Change: {change:.2f} EGP")

print("\n========== THANK YOU ==========")
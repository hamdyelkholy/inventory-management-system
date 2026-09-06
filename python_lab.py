# Task 01
name1, name2 = input("Enter two student names: ").split()
score1, score2 = 85.5, 92.0

name1, name2 = name2, name1
score1, score2 = score2, score1

print("[RECORD]", name1, score1, name2, score2,
      sep=" ::: ",
      end="\n--- FINISHED RECORD ---\n")

total_score = score1 + score2
total_int = int(total_score)
total_string = str(total_score)

print("Total Score (Int):", total_int,
      "| Total Score (Type):", type(total_string))

del total_score


# Task 02
amount = float(input("Enter order amount: "))
country = input("Enter country: ").lower()

duty_free_countries = ['egypt', 'uae', 'saudi', 'kuwait']

eligible = amount >= 500.0 and country in duty_free_countries

free_shipping = "Free Express Shipping"
standard_shipping = "Standard Shipping (50 EGP)"

status = free_shipping if eligible else standard_shipping

vip_flag = status is free_shipping

print("Delivery:", status, "| VIP Logistics Flag:", vip_flag)


# Task 03
units = float(input("Enter units consumed: "))
acc_type = input("Enter account type (res/com): ").strip().lower()

if units < 0 or acc_type not in ['res', 'com']:
    print("Invalid Input")
else:
    if units <= 100:
        base_bill = units * 0.75
    elif units <= 250:
        base_bill = (100 * 0.75) + ((units - 100) * 1.20)
    else:
        base_bill = (100 * 0.75) + (150 * 1.20) + ((units - 250) * 1.80)

    if acc_type == 'res':
        tax = base_bill * 0.05
    else:
        tax = (base_bill * 0.12) + 20.0

    total = base_bill + tax
    print("Base Bill:", base_bill, "EGP | Tax:", tax, "EGP | Total Due:", total, "EGP")


# Task 04
code = int(input("Enter HTTP status code: "))

match code:
    case 200 | 201:
        msg = 'SUCCESS: Request fulfilled and resource ready.'
    case 400 | 422:
        msg = 'CLIENT ERROR: Bad request or unprocessable payload.'
    case 401 | 403:
        msg = 'ACCESS DENIED: Authentication required or forbidden.'
    case 404:
        msg = 'NOT FOUND: The requested resource does not exist.'
    case 500 | 502 | 503:
        msg = 'SERVER ERROR: Upstream server is unavailable.'
    case _:
        msg = 'UNKNOWN CODE: Protocol response code unmapped.'

print("[Response", str(code) + "]", msg)


# Task 05
start = int(input("Enter start: "))
stop = int(input("Enter stop: "))
step = int(input("Enter step: "))

results = []

for num in range(start, stop, step):
    if num > 80:
        break
    if num % 3 == 0 or num % 10 == 5:
        continue
    results.append(str(num))

results.append("[SCAN COMPLETE]")
print(" # ".join(results))


# Task 06
N = int(input("Enter N (3-6): "))

for i in range(1, N + 1):
    row = []
    for j in range(1, N + 1):
        if i == j:
            row.append("[X]".center(6))
        else:
            row.append(f"({i},{j})".center(6))
    print("".join(row))


# Task 07
stock = 50
restocks = 0
dispatches = 0

while True:
    qty = int(input("Enter quantity adjustment (0 to stop): "))
    
    if qty == 0:
        break
    elif qty > 0:
        stock += qty
        restocks += 1
    else:
        dispatch_qty = abs(qty)
        if dispatch_qty > stock:
            print("Dispatch Rejected: Insufficient inventory")
        else:
            stock -= dispatch_qty
            dispatches += 1
            if stock == 0:
                print("Warning: Stock Depleted!")

print("[INVENTORY FINAL REPORT] Current" \
"Units:", stock, "| Restocks:", restocks, "| Dispatches:", dispatches)





# Bonus
subtotal = 0.0

print("(1) Standard 2D Ticket - 80 EGP")
print("(2) IMAX 3D Ticket - 130 EGP")
print("(3) VIP Recliner Ticket - 200 EGP")
print("(4) Popcorn Combo - 45 EGP")
print("(5) Soda Beverage - 25 EGP")
print("(0) Proceed to Payment")

while True:
    user_input = input("Enter item number and quantity: ").split()
    item_num = int(user_input[0])
    
    if item_num == 0:
        break
        
    qty = int(user_input[1])
    price = 0
    
    match item_num:
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
            price = 0
            
    subtotal += price * qty

discount = subtotal * 0.10 if subtotal > 250 else 0.0
final_bill = subtotal - discount

print("Subtotal:", subtotal, "EGP")
print("Discount Applied:", discount, "EGP")
print("Final Bill:", final_bill, "EGP")

paid = 0.0
while paid < final_bill:
    paid += float(input("Enter cash tendered: "))

change = paid - final_bill

print("\n--- SUMMARY ---")
print("Total Paid:", paid, "EGP")
print("Change Returned:", change, "EGP")
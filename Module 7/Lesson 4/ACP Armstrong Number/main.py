
# Armstrong Number Checker
print("===== ARMSTRONG NUMBER CHECKER =====")

# Part 1: Ask for a number
number = input("Enter a number: ")

# Part 2: Count the digits
digit_count = len(number)
print(f"Number of digits: {digit_count}")

total = 0

# Part 3: Loop through each digit
for digit in number:
    power = int(digit) ** digit_count
    print(f"{digit} to the power {digit_count} = {power}")
    total += power

# Part 4: Show the result
print(f"Sum of the powers = {total}")

if total == int(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

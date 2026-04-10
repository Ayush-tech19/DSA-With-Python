num = int(input("Enter a number: "))

# Count the number of digits
n = len(str(num))

temp = num
sum = 0

# Calculate sum of digits raised to the power n
while temp > 0:
    digit = temp % 10        # Get last digit
    sum += digit ** n        # Add digit^n to sum
    temp //= 10              # Remove last digit

# Check if it is an Armstrong number
if sum == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
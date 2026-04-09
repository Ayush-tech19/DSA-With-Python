num = int(input("Enter a number: "))
num = abs(num)

count = 0

if num == 0:
    count = 1
else:
    while num > 0:
        digit = num % 10   # last digit extract
        count += 1         # digit count
        num = num // 10    # last digit remove

print("Total digits:", count)
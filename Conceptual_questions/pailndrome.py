# Check palindrome string

string = input("Enter a string: ")

# reverse string
rev = string[::-1]

if string == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
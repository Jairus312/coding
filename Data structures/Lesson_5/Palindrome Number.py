Number = int(input("Enter the Number :-"))
original_number = Number
reversed_number = 0

while Number > 0:
    digit = Number % 10 
    reversed_number = reversed_number * 10 + digit
    Number //= 10

if original_number == reversed_number:
    print(f"{original_number    } is a panlindrome.")

else:
    print(f"{original_number} is not a panlindrome.")
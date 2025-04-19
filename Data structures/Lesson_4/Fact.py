def print_number(number):
    print("factor of",number,"are")
    for i in range(1, number+1):
        if number % i == 0:
            print(i)

number = int(input("Enter a  number to find a factor :-" \
"")) 
print_number(number)              
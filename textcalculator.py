def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")

select = int(input("Select an operation from 1 to 4."))

num_1 = int(input("Please enter the first number."))
num_2 = int(input("Please enter the second number"))

if select == 1:
    print(num_1, '+', num_2, '=', add(num_1, num_2))

elif select == 2:
    print(num_1, "-", num_2, "=",
                    subtract(num_1, num_2))

elif select == 3:
    print(num_1, "*", num_2, "=",
                    multiply(num_1, num_2))

elif select == 4:
    print(num_1, "/", num_2, "=",
                    divide(num_1, num_2))
else:
    print("Invalid input")

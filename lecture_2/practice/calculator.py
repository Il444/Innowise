def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: cannot divide by zero"
        return num1 / num2
    elif operator == '%':
        if num2 == 0:
            return "Error: cannot divide by zero"
        return num1 % num2
    elif operator == '//':
        if num2 == 0:
            return "Error: cannot divide by zero"
        return num1 // num2
    elif operator == '**':
        return num1 ** num2
    else:
        return "Invalid operator"

def main():
    print("Simple calculator")
    print("Operators: +, -, *, /, //, %, **")

    num1 = int(input("Enter first number: "))
    operator = input("Enter operator: ")
    num2 = int(input("Enter second number: "))

    result = calculate(num1, operator, num2)

    print(f"{num1} {operator} {num2} = {result}")

if __name__ == "__main__":
    main()
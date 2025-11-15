n1 = int(input())
n2 = int(input())
op = input()

result = 0
even_or_odd = ""
error_message = ""

if op == "+" or op == "-" or op == "*":
    if op == "+":
        result = n1 + n2
    elif op == "-":
        result = n1 - n2
    elif op == "*":
        result = n1 * n2

    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
elif op == "/":
    if n2 == 0:
        error_message = (f"Cannot divide {n1} by zero")
    else:
        result = n1 / n2
elif op == "%":
    if n2 == 0:
        error_message = (f"Cannot divide {n1} by zero")
    else:
        result = n1 % n2

if op == "+" or op == "-" or op == "*":
    print(f"{n1} {op} {n2} = {result} - {even_or_odd}")
elif op == "/":
    if n2 != 0:
        print(f"{n1} {op} {n2} = {result:.2f}")
    else:
        print(error_message)
elif op == "%":
    if n2 != 0:
        print(f"{n1} {op} {n2} = {result}")
    else:
        print(error_message)

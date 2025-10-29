
a = float(input("Wpiś pierwszą liczbę"))
c = input("Wpis znak")
b = float(input("Wpiś drrugą liczbę"))

if c == "+":
    print(a+b)
elif c == "-":
    print(a-b)
elif c == "*":
    print(a*b)
elif c == "/":
    print(a/b)
elif c == "^":
    print(a**b)
else:
    print("To nie jest znakiem")
from math import sqrt

a =int(input("liczba 1"))
b =int(input("liczba 2"))
c =int(input("liczba 3"))

d = b**2-(4*a*c)

if d > 0:
    print((sqrt(d)-b)/(2*a))
    print((-1*(sqrt(d) + b)) / (2 * a))
elif d ==0:
    print(-1*(b/(2*a)))
else:
    print("Nie ma")
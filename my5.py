x = input("Введіть кількість робочих годин")
y = input("Ставка")
try:
    a = float(x)
    b = float(y)
except:
    print("Введіть число знову")
    quit()
if a <= 40:
    c = a * 40
else:
    c = 40 * b + (a - 40) * b * 2
    print(c)
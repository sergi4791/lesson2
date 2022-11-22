TAX_RATE = 0.05
TIP_RATE = 0.18
cost = float(input("Введите сумму счета: "))
# Вычисляем сумму налога и чаевых
tax = cost * TAX_RATE
tip = cost * TIP_RATE
total = cost + tax + tip
# Отобразим результат
print("Налог составил $%.2f, чаевые – $%.2f, общая сумма заказа: $%.2f" % (tax, tip, total))
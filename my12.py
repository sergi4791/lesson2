# back_counter = 99
# end_value = 0
# while back_counter > end_value:
#     if back_counter % 5 == 0:
#         print(back_counter)
#     back_counter -= 1

number = 0
str_ = "Enter a positive integer: "
while number <= 0:
    number = int(input(str_))
    if number >= 0:

print("You have entered", number)
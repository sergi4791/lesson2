# # int_list = [1,2,3,4]
# # print(int_list)
# #
# # list_from_range = list(range(5))
# # print(list_from_range)
# #
# # my_list = [5, 7, 9, 1, 1, 2]
# #
# # print(my_list[0])
# # print(my_list[1])
# # index = int(input('Enter index: '))
# # element = my_list[index]
# # print(element)
#
# my_list = [5, 7, 9, 1, 1, 2]
# my_list1 = my_list[0:3]
# print(my_list1)
#
# print(my_list[2:-2])
# print(my_list[4:5])
#
# my_list1 = my_list[::-1]
# print(my_list1)
#
# print(my_list[::-2])


# my_list = [5, 7, 9, 1, 1, 2]
#
# value = int(input('enter a numer: '))
# if value in my_list:
#     print('Thus number is in list')
# else:
#     print('This number is not in list')
# # #

# my_list = [5, 7, 9, 1, 1, 2,8]
# print(len(my_list))
#
# string = "a string"
# print(string[0])
# print(string[2])
# print(string[-1])
#
# print(string[2:])
# print(string[::2])
# print(string[::-1])
#
# print(string[2] + string[-3:])
#
# # string = input('Enter a string: ')
# # if 'q' in string:
# #     print("There's a 'q' in the string")
# # else:
# #     print("There isn't a 'q' in the string")
#
# my_list = []
# my_list.append(3)
# my_list.append(5)
# my_list.append(my_list[0] + my_list[1])
# print(my_list)
#
# my_list = [5, 7, 9, 1, 1, 2, -23]
#
# for x in my_list:
#     print("{} ^ 2 = {}".format(x, x ** 2))

    #fibanocci
n = 10

fib = [1, 1]

for i in range(n - 2):
    fib.append(fib[i] + fib)[i + 1]

print(fib)
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# n = input()
# summ = 0
# for i in n:
#     if i.isdigit():
#         summ+=int(i)
# print(summ)

# n = float(input())
# len_num = len(str(n))-1
# summ=0
# while n!=int(n):
#     n= round(n*10,len_num)
#     print(n)
# while n>0:
#     summ+=n%10
#     n = n//10
# print(summ)






# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input())
# #пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# fact_list = []
# factorial = 1
# for i in range(1,n+1):
#     factorial*=i
#     fact_list.append(factorial)
# print(fact_list)



# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#         Сумма 9.06


n = int(input())
dict_num = {}
for i in range(1,n+1):
    dict_num[i] = round((1+1/i)**i,2)
print(dict_num)
print(sum(dict_num.values()))


# 4 задача


# import random
#
# n = int(input())
# list_num = [random.randint(-n,n) for i in range(n)]
# print(list_num)

# file = open("File.txt","r")
# multi = 1
# list_str = file.readlines()
# print(list_str)
# list_num = list(map(str.strip,list_str))
# print(list_num)
# list_num = list(map(int,list_num))
# print(list_num)
# for i in file:
#     multi*=list_num[int(i)]
# print(multi)









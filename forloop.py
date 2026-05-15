"""LIst """

# my_list = []
# my_list.append("Elements")
# my_list.append("Sub")
# my_list.extend([12 , 56, True])
# my_list.insert(0, "Javohir")
# print(my_list)

# """O"chirish operatorlari"""
# names = ["Tom", "Edson", "Siril", "Elements", "Smart"]
# names.remove("Tom")
# print(names)
# del names[-1]
# print(names)
# print(names.pop(2))
# print(names)
# names.clear()
# print(names)

# numbers = [10 , 20 , 30 , 40 , 50 ]
# """
# 1 . 20 elementini listdan o'chiring 
# 2. 60 elementini listga qo'shing 
# """




# names = ["Tom", "Edson", "Siril", "Elements", "Smart"]
# for i in names:
#     print(i)


""" For loop """
# names = ["Tom", "Edson", "Siril", "Elements", "Smart"]
# for i in names:
#     if "e" in i.lower(): 
#         print(i)

# name = input("Ism yoz")
# for j in name:
#     print(j)

"""1 dan 10 gacha"""
# raqam = 10
# for i in range(1, raqam+1): 
#     print(i)

# raqam = 10
# for i in range(1, raqam+1): 
#     if i % 2 == 0: 
#         print(i)


# n = 100
# sum = 0 
# for i in range(1 , n+1):
#     sum = sum + i
# print(sum)


import random 
son = random.randint(1 , 50)
print("Men son o'yladim sen top")
urinishlar = 5 
while urinishlar >0: 
    urinishlar = urinishlar - 1
    your_number = int(input("Son kirit? "))
    if your_number >son: 
        print(f"KIchikroq son kirit? \nSenda {urinishlar} urnish qoldi" )
    elif your_number < son: 
        print(f"Kattaroq son kirit. \nSenda {urinishlar} urnish qoldi")
    else: 
        print(f" Sen  topding. {son}")
        break
    
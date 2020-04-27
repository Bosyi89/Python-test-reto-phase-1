# Generate 2 lists with the length of 10 with random integers from 1 to 10
# make a third list containing the common integers between the 2 initial lists without any duplicates. (щоб не дублювалися)
# use only while loop and random module to generate numbers


import random


list_1 = []
list_2 = []
list_3 = []
i = 0
while i != 10:
    list_1.append(random.randint(1, 10))
    list_2.append(random.randint(1, 10))
    a = i
    while a >= 0:
        if list_1[a] in list_2 and list_1[a] not in list_3:
            list_3.append(list_1[a])
        a -= 1
    i += 1
print(list_1)
print(list_2)
print(list_3)

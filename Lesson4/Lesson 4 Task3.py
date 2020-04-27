#Make a list that contains all integers from 1 to 100
#divisible by 7
# not a multiple of 5


a = 0
our_list = []
special_list = []
while a < 100:
	our_list.append(a + 1)
	if (a + 1) % 7 == 0 and (a + 1) % 5 != 0:
		special_list.append(a+ 1)
	a += 1
print(our_list)
print()
print(special_list)

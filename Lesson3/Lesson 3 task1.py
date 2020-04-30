
#first 2 and the last 2 chars from a given string. 
#If the string length is less than 2, return instead of the empty string.
#Sample String: 'helloworld'
#Expected Result : 'held'

#Sample String: 'my'
#Expected Result : 'mymy'

#Sample String: ' x'
#Expected Result: Empty String
# use only []


string1 = input('Введіть слово:')
string2 = string1.strip()
if len(string2) >= 2:
	print(string2[0:2] + string2[-2] + string2[-1])
else:
	print('Empty String')
print()
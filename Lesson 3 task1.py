
#first 2 and the last 2 chars from a given string. 
#If the string length is less than 2, return instead of the empty string.
#Sample String: 'helloworld'
#Expected Result : 'held'

#Sample String: 'my'
#Expected Result : 'mymy'

#Sample String: ' x'
#Expected Result: Empty String
# use only []


a = input()
if len(a) > 2:
	print(a[0:2] + a[-2] + a[-1])
if len(a) < 2:
	print()

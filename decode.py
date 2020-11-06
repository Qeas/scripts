import string

letters = list(string.ascii_lowercase)
d = {}
for i in range(1, 27):
	d[letters[i - 1]] = i

def decode(input_string):
	result = 0
	if not input_string:
		return 1
	elif input_string.startswith('0'):
		return 0
	if len(input_string) >= 2 and int(input_string[:2]) in d.values():
		result = decode(input_string[2:]) + decode(input_string[1:])
	else:
		result = decode(input_string[1:])
	return result

print(decode('111111'))


# ""
# '12' + decode(345) + '1' + decode(2345)
# '3' + decode(45)
# '4' + decode(5) == 1


# 3 + 
# ""
import sys

def solution(input_string):
	while True:
		new_num = 0
		for i in str(input_string):
			new_num += int(i)
		if new_num // 10 == 0:
			return new_num
		input_string, new_num = new_num, 0


print(solution(83))
given_set = [1,3,2,5,6,7]

for k, v in enumerate(given_set):
	subset = [v]
	print(subset)
	for i in range(k + 1, len(given_set)):
		subset.append(given_set[i])
		print(subset)
		if len(subset) > 2:
			print([v, given_set[i]])

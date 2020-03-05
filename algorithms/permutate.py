def permutate(items):
	if len(items) == 1:
		return [items]

	combos = []

	for i in range(len(items)):
		c = items[i]
		remain = items[:i] + items[i+1:]
		for x in permutate(remain):
			combos.append([c] + x)
	return combos



items = [1,2,3,4]
p = permutate(items)
print(p)
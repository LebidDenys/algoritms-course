def fibonacci_words(string_one, string_two, digit):
	length_one, length_two = len(string_one), len(string_two)
	if length_one >= digit:
		return string_one[digit - 1]
	if length_two > digit:
		return string_two[digit - 1]

	length_array = [length_one, length_two]
	index = 1
	for i in range(2, digit + 1):
		index += 1
		new = length_array[i - 2] + length_array[i - 1]
		length_array.append(new)
		if new >= digit:
			break

	temp = digit
	while index > 1:
		if length_array[index - 2] < temp:
			temp = temp - length_array[index - 2]
			index -= 1
		else:
			index -= 2

	if index == 0:
		return string_one[temp - 1]
	else:
		return string_two[temp - 1]


n = int(input())
for i in range(n):
	(s_one, s_two, d) = input().strip().split()
	result = fibonacci_words(s_one, s_two, int(d))
	print(result)

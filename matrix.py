import fileinput


def processData(rawData):
	# rawData = ""
	# for line in fileinput.input():
	# 	rawData += line
	arr = []
	[size, index] = [int(i) for i in rawData.split(" ")]

	for i in range(size):
		arr.append(i)


data = "1 1"
print(processData(data))
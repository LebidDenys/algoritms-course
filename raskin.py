import fileinput


def processData():
	rawData = ""
	for line in fileinput.input():
		rawData += line

	inputData = rawData.split("\n")

	for i in range(0, int(inputData[0]) * 3, 3):
		solutuin = getSolution(int(inputData[i + 1]), int(inputData[i + 2]), inputData[i + 3].split(' '))
		print(solutuin)


def getSolution(summ, arrLen, arr):
	dict = {}
	for priceIndex in range(len(arr)):
		if arr[priceIndex] not in dict:
			dict[int(arr[priceIndex])] = priceIndex

	for priceIndex in range(len(arr)):
		diff = summ - int(arr[priceIndex])
		if diff in dict and dict[diff] != priceIndex:
			return str(min(priceIndex, dict[diff]) + 1) + " " + str(max(priceIndex, dict[diff]) + 1)


processData()

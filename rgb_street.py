import fileinput


def processData():
	rawData = ""
	for line in fileinput.input():
		rawData += line

	inputData = rawData.split("\n")
	firstLine = inputData[1].split(' ')
	resultRed, resultGreen, resultBlue = int(firstLine[0]), int(firstLine[1]), int(firstLine[2])
	for i in range(2, int(inputData[0]) + 1):
		currentLine = inputData[i].split(' ')
		currentRed = int(currentLine[0]) + min(resultGreen, resultBlue)
		currentGreen = int(currentLine[1]) + min(resultRed, resultBlue)
		currentBlue = int(currentLine[2]) + min(resultGreen, resultRed)
		resultRed, resultGreen, resultBlue = currentRed, currentGreen, currentBlue

	return min(resultRed, resultGreen, resultBlue)


res = processData()
print(res)

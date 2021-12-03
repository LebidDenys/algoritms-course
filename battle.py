import fileinput


def processData():
	rawData = ""
	for line in fileinput.input():
		rawData += line

	inputData = rawData.split("\n")
	playerUnits = [int(i) for i in inputData[1].split(" ")]
	computerUnits = [int(i) for i in inputData[2].split(" ")]
	playerUnits.sort()
	computerUnits.sort()
	res, shiftingIndex = 0, 0
	for i in range(int(inputData[0]) - 1, -1, -1):
		if playerUnits[i] > computerUnits[i]:
			res = res + playerUnits[i]
		else:
			playerUnits.append(playerUnits.pop(0))
	return res

# data = "5\n5 15 100 1 5\n5 15 100 1 5"
# data = "50\n651 321 106 503 227 290 915 549 660 115 491 378 495 789 507 381 685 530 603 394 7 704 101 620 859 490 744 495 379 781 550 356 950 628 177 373 132 740 946 609 29 329 57 636 132 843 860 594 718 849\n16 127 704 614 218 67 169 621 340 319 366 658 798 803 524 608 794 896 145 627 401 253 137 851 67 426 571 302 546 225 311 111 804 135 284 784 890 786 740 612 360 852 228 859 229 249 540 979 55 82"
print(processData(data))

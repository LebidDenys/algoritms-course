import fileinput


def processData():
    rawData = ""
    for line in fileinput.input():
        rawData += line
    inputData = rawData.split("\n")
    numberOfLines, totalZeros, totalOnes = [int(i) for i in inputData[0].split(" ")]
    dp = [[0 for _ in range(totalOnes + 1)] for _ in range(totalZeros + 1)]
    for r in range(1, numberOfLines + 1):
        line = inputData[r]
        zeros = line.count("0")
        ones = len(line) - zeros
        for i in range(totalZeros, zeros - 1, -1):
            for j in range(totalOnes, ones - 1, -1):
                dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
    return dp[totalZeros][totalOnes]


print(processData())

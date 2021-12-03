import fileinput


def processData():
    rawData = ""
    for line in fileinput.input():
        rawData += line

    inputData = rawData.split("\n")
    n, start, end = [int(i) for i in inputData[0].split(" ")]
    legal_moves = [int(i) for i in inputData[1].split(" ")]
    memory = [0] * (end + 1)
    result = 0
    for i in range(start, end + 1):
        result = result + 1 if whoWins(memory, i, legal_moves) == 1 else result
    return result


def whoWins(memory, stones_quantity, moves):
    if stones_quantity == 0:
        memory[0] = 2
        return 2
    else:
        for i in range(len(moves)):
            if stones_quantity - moves[i] >= 0 and memory[stones_quantity - moves[i]] == 2:
                memory[stones_quantity] = 1
                return 1
            elif stones_quantity - moves[i] >= 0 and memory[stones_quantity - moves[i]] == 0 and whoWins(memory, stones_quantity - moves[i], moves) == 2:
                memory[stones_quantity] = 1
                return 1
        memory[stones_quantity] = 2
        return 2


print(processData())

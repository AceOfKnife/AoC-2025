def findLargestJoltage(bank):
    n = len(bank)
    prev = ['0'] * n
    curr = ['0'] * n

    prev[-1] = bank[-1]
    for i in reversed(range(n - 1)):
        prev[i] = max(bank[i], prev[i+1])
    
    for i in range(2, 13):
        limit = n - i
        curr[limit] = bank[limit] + prev[limit + 1]
        for j in reversed(range(limit)):
            curr[j] = max(bank[j] + prev[j+1], curr[j+1])
        prev, curr = curr, prev

    return int(prev[0])

def getLargestSuffix(banks):
    largestSuffix = []

    for bank in banks:
        suffix = [0] * len(bank)
        suffix[-1] = bank[-1]
        for i in reversed(range(len(bank) - 1)):
            suffix[i] = max(bank[i], suffix[i+1])
        largestSuffix.append(suffix)
    
    return largestSuffix

def main():

    banks = []

    with open("day3.txt") as batteryJolts:
        for bank in batteryJolts:
            banks.append(bank.replace("\n", ""))
    
    largestSuffix = getLargestSuffix(banks)
    
    totalJoltage = 0

    for bank, suffix in zip(banks, largestSuffix):
        maxJoltage = 0
        for i in range(len(bank) - 1):
            maxJoltage = max(maxJoltage, int(bank[i] + suffix[i+1]))
        totalJoltage += maxJoltage
    
    print("Part 1:", totalJoltage)

    totalJoltage = 0

    for bank in banks:
        totalJoltage += findLargestJoltage(bank)
    
    print("Part 2:", totalJoltage)

if __name__=="__main__":
    main()
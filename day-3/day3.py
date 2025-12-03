def findLargestJoltage(bank):
    n = len(bank)
    dp = [['0' for _ in range(n)] for _ in range(13)]
    
    dp[1][-1] = bank[-1]
    for i in reversed(range(len(bank) - 1)):
        dp[1][i] = max(bank[i], dp[1][i+1])
    
    for i in range(2, 13):
        for j in reversed(range(n - i + 1)):
            dp[i][j] = max(bank[j] + dp[i-1][j+1], dp[i][j+1])
    return int(dp[12][0])

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
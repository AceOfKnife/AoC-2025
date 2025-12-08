def calculateColumn(mathHomework, end):
    start = end - 1
    nums = []
    while start >= 0:
        num = 0
        for i in range(len(mathHomework) - 1):
            if mathHomework[i][start] != ' ':
                num *= 10
                num += int(mathHomework[i][start])
        nums.append(num)
        if mathHomework[-1][start] == '*':
            res = 1
            for num in nums:
                res *= num
            return res, start - 1
        if mathHomework[-1][start] == '+':
            return sum(nums), start - 1
        start -= 1
    return None

def main():
    
    mathHomework = []

    with open("day6.txt") as mathInput:
        for line in mathInput:
            mathHomework.append(line.replace("\n", ""))
    
    end = len(mathHomework[0])
    total = []
    while end > 0:
        res, end = calculateColumn(mathHomework, end)
        total.append(res)
    print("Part 2:", sum(total))

        
if __name__=="__main__":
    main()
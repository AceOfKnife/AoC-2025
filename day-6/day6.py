def main():
    
    numbers = []

    with open("day6-test.txt") as mathHomework:
        op = set(('+', '*'))
        for line in mathHomework:
            tmp = []
            curr = ''
            for c in line:
                if c == ' ' or c == '\n':
                    if curr != '':
                        tmp.append(int(curr))
                        curr = ''
                elif c in op:
                    tmp.append(c)
                else:
                    curr += c
            numbers.append(tmp)
        
    total = 0
    
    n, m = len(numbers), len(numbers[0])
    
    for problem in range(m):
        operator = numbers[-1][problem]
        if operator == '+':
            tmp = 0
            for i in range(n-1):
                tmp += numbers[i][problem]
        else:
            tmp = 1
            for i in range(n-1):
                tmp *= numbers[i][problem]
        total += tmp
    print("Part 1:", total)
        
if __name__=="__main__":
    main()
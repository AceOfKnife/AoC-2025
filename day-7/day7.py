from collections import deque 

def dfs(tachyonDiagram, x, y, memo):
    if (x,y) not in memo:
        n, m = len(tachyonDiagram), len(tachyonDiagram[0])
        splitX = x + 1
        while splitX < n and tachyonDiagram[splitX][y] == '.':
            splitX += 1

        if splitX >= n:
            return 1
        
        left = y - 1
        right = y + 1
        count = 0
        if left >= 0:
            count += dfs(tachyonDiagram, splitX, left, memo)
        if right < m:
            count += dfs(tachyonDiagram, splitX, right, memo)
        memo[(x,y)] = count
    return memo[(x,y)]

def main():
    
    tachyonDiagram = []

    with open("day7.txt") as tachyonInput:
        for line in tachyonInput:
            tachyonDiagram.append(line.replace("\n", ""))
    
    n, m = len(tachyonDiagram), len(tachyonDiagram[0])
    starting = 0
    for col in range(m):
        if tachyonDiagram[0][col] == 'S':
            starting = col
    
    q = deque([starting])
    splits = 0
    level = 0
    while level < n - 1:
        seen = set()
        for _ in range(len(q)):
            col = q.popleft()
            if tachyonDiagram[level+1][col] == '.' and col not in seen:
                seen.add(col)
                q.append(col)
            elif tachyonDiagram[level+1][col] == '^':
                splits += 1
                left, right = col - 1, col + 1
                if left >= 0 and left not in seen:
                    seen.add(left)
                    q.append(left)
                if right >= 0 and right not in seen:
                    seen.add(right)
                    q.append(right)
        level += 1
    
    print("Part 1:", splits)

    print("Part 2:", dfs(tachyonDiagram, 0, starting, {}))
        
if __name__=="__main__":
    main()
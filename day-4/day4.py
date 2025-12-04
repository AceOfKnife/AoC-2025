def canAccess(x, y, map):
    n, m = len(map), len(map[0])
    directions = ((-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1))
    count = 0
    for dx, dy in directions:
        ddx, ddy = x + dx, y + dy
        if 0 <= ddx < n and 0 <= ddy < m:
            count += 1 if map[ddx][ddy] == '@' else 0
    return count < 4

def main():

    map = []

    with open("day4.txt") as mapFile:
        for row in mapFile:
            map.append([x for x in row if x != '\n'])
    
    n, m = len(map), len(map[0])
    papers = 0

    for i in range(n):
        for j in range(m):
            if map[i][j] == '@':
                papers += 1 if canAccess(i, j, map) else 0
    
    print("Part 1:", papers)

    papers = 0

    extractingPapers = True
    
    while extractingPapers:
        extractingPapers = False
        for i in range(n):
            for j in range(m):
                if map[i][j] == '@':
                    if canAccess(i, j, map):
                        extractingPapers = True
                        papers += 1
                        map[i][j] = '.'
    
    print("Part 2:", papers)
    

if __name__=="__main__":
    main()
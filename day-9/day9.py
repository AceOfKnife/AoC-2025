from collections import deque
import time

def computeRectangleArea(tile1, tile2):
    x1, y1 = tile1
    x2, y2 = tile2

    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

def getFourCorners(corner1, corner2):
    x1, y1 = corner1
    x2, y2 = corner2

    return corner1, (x1, y2), (x2, y1), corner2

def findBoundary(tile, xMax, yMax, boundary):
    q = deque([(tile[0], tile[1], 0, -1), (tile[0], tile[1], 1, 0), (tile[0], tile[1], 0, 1), (tile[0], tile[1], -1, 0)])

    while q:
        x, y, dx, dy = q.popleft()
        if (x, y) in boundary:
            continue
        if x < 0 or x > xMax or y < 0 or y > yMax:
            return False
        ddx, ddy = x + dx, y + dy
        q.append((ddx, ddy, dx, dy))
    
    return True

def floodFill(xStart, yStart, grid):
    q = deque([(xStart, yStart)])
    directions = ((0,1), (1,0), (0,-1), (-1,0))
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            ddx, ddy = x + dx, y + dy
            if grid[ddy][ddx] == 0:
                grid[ddy][ddx] = 1
                q.append((ddx, ddy))

def main():

    redTiles = []
    with open("day9-test.txt") as redTilesInput:
        for line in redTilesInput:
            redTiles.append(tuple(map(int, line.split(","))))
    
    largestArea = 0
    for i in range(len(redTiles)):
        for j in range(i+1, len(redTiles)):
            largestArea = max(largestArea, computeRectangleArea(redTiles[i], redTiles[j]))
    
    print("Part 1:", largestArea)

    start = time.time()
    largestArea = 0
    n, m = max(redTiles, key=lambda x: x[0])[0] + 1, max(redTiles, key=lambda x: x[1])[1] + 1
    grid = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(len(redTiles)):
        x1, y1 = redTiles[i]
        x2, y2 = redTiles[(i+1) % len(redTiles)]
        if x1 == x2:
            for j in range(min(y1, y2), max(y1, y2) + 1):
                grid[j][x1] = 1
        else:
            for j in range(min(x1, x2), max(x1, x2) + 1):
                grid[y1][j] = 1
                
    xAvg, yAvg = sum([x[0] for x in redTiles]) // len(redTiles), sum([y[1] for y in redTiles]) // len(redTiles)
    floodFill(xAvg, yAvg, grid)

    for i in range(len(redTiles)):
        for j in range(i+1, len(redTiles)):
            c1, c2, c3, c4 = getFourCorners(redTiles[i], redTiles[j])
            if all(grid[y][x] == 1 for x, y in (c1, c2, c3, c4)):
                largestArea = max(largestArea, computeRectangleArea(redTiles[i], redTiles[j]))

    end = time.time()
    print("Part 2:", largestArea)
    print(end - start, "seconds")
    
if __name__=="__main__":
    main()
import heapq
import math
from collections import deque

def bfs(q, adjList, seen):
    numNodes = 0
    while q:
        node = q.popleft()
        numNodes += 1
        for adjNode in adjList[node]:
            if adjNode not in seen:
                seen.add(adjNode)
                q.append(adjNode)
    return numNodes

def computeDistance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)

def main():

    junctionBoxes = []
    with open("day8.txt") as junctionBoxCoordinates:
        for line in junctionBoxCoordinates:
            junctionBoxes.append(tuple(map(int, line.split(","))))
    
    distancePairs = []
    for i in range(len(junctionBoxes)):
        for j in range(i+1, len(junctionBoxes)):
            heapq.heappush(distancePairs, (computeDistance(junctionBoxes[i], junctionBoxes[j]), (i, j)))
    
    adjList = [[] for _ in range(len(junctionBoxes))]

    while bfs(deque([0]), adjList, set([0])) < len(junctionBoxes):
        _, (j1, j2) = heapq.heappop(distancePairs)
        adjList[j1].append(j2)
        adjList[j2].append(j1)
    
    print("Part 2:", junctionBoxes[j1][0] * junctionBoxes[j2][0])

if __name__=="__main__":
    main()
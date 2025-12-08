import heapq

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.size[pa] < self.size[pb]:
            pa, pb = pb, pa
        self.parent[pb] = pa
        self.size[pa] += self.size[pb]
        self.components -= 1
        return True

def computeDistanceSquared(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    return (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2

def main():

    junctionBoxes = []
    with open("day8.txt") as junctionBoxCoordinates:
        for line in junctionBoxCoordinates:
            junctionBoxes.append(tuple(map(int, line.split(","))))
    
    distancePairs = []
    for i in range(len(junctionBoxes)):
        for j in range(i+1, len(junctionBoxes)):
            heapq.heappush(distancePairs, (computeDistanceSquared(junctionBoxes[i], junctionBoxes[j]), i, j))
    
    dsu = DSU(len(junctionBoxes))
    
    while dsu.components > 1:
        _, a, b = heapq.heappop(distancePairs)
        merged = dsu.union(a, b)
        if merged:
            lastA, lastB = a, b
    
    print("Part 2:", junctionBoxes[lastA][0] * junctionBoxes[lastB][0])

if __name__=="__main__":
    main()
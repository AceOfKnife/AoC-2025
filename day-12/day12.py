def main():

    shapes = []
    regions = []
    with open("day12.txt") as shapesAndRegions:
        for _ in range(6):
            shape = []
            shapesAndRegions.readline()
            for _ in range(3):
                row = shapesAndRegions.readline()
                shape.append([0 if row[i] == '.' else 1 for i in range(3)])
            shapesAndRegions.readline()
            shapes.append(shape)

        for line in shapesAndRegions:
            i = 0
            while line[i] != ':':
                i += 1
            key = tuple(map(int, line[:i].split("x")))
            i += 2
            freq = tuple(map(int, line[i:].replace("\n", "").split(" ")))
            regions.append((key, freq))
    
    possible = 0
    impossible = 0
    maybe = 0
    for region, presents in regions:
        area = region[0] * region[1]
        markedPresents = 0
        for i in range(len(presents)):
            markedPresents += presents[i] * sum(map(sum, shapes[i]))
        if area >= 9 * sum(presents):
            possible += 1
        elif markedPresents > area:
            impossible += 1
        else:
            maybe += 1
    
    print("Possible:", possible)
    print("Impossible:", impossible)
    print("Maybe:", maybe)

    
if __name__=="__main__":
    main()
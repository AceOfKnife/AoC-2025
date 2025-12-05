def isFresh(ingredient, freshRanges):
    left, right = 0, len(freshRanges) - 1

    while left <= right:
        mid = left + (right - left) // 2
        start, end = freshRanges[mid]
        if ingredient < start:
            right = mid - 1
        elif ingredient > end:
            left = mid + 1
        else:
            return True
    
    return False

def mergeRanges(freshRanges):

    startAndEnds = []
    for start, end in freshRanges:
        startAndEnds.append((start, +1))
        startAndEnds.append((end, -1))
    startAndEnds.sort(key = lambda x: (x[0], -x[1]))

    mergedRanges = []
    active = 0
    curr = [0,0]
    for id, value in startAndEnds:
        if active == 0:
            curr[0] = id
        active += value
        if active == 0:
            curr[1] = id
            mergedRanges.append(curr[:])
    
    return mergedRanges

def main():

    freshRanges = []
    ingredients = []

    with open("day5.txt") as ingredientIDs:
        parseRanges = True
        for row in ingredientIDs:
            if row == '\n':
                parseRanges = False
                continue
            if parseRanges:
                freshRanges.append([int(x) for x in row.split("-")])
            else:
                ingredients.append(int(row))

    freshRanges = mergeRanges(freshRanges)

    available = 0

    for ingredient in ingredients:
        available += 1 if isFresh(ingredient, freshRanges) else 0
    
    print("Part 1:", available)

    print("Part 2:", sum([end - start + 1 for start, end in freshRanges]))

if __name__=="__main__":
    main()
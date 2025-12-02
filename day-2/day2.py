def findAllInvalid(number: int) -> bool:
    idString = str(number)
    n = len(idString)
    for repeats in range(2, n+1):
        invalid = True
        if n % repeats != 0:
            continue

        last = n // repeats
        idToMatch = set([idString[:last]])
        
        for i in range(0, n, last):
            if idString[i:i+last] not in idToMatch:
                invalid = False
                break
        
        if invalid:
            return True
    return False


def findInvalid(number: int) -> bool:
    idString = str(number)
    if len(idString) % 2 == 1:
        return False
    right = len(idString) // 2

    for left in range(len(idString) // 2):
        if idString[left] != idString[right]:
            return False
        right += 1
    return True

def main():

    idRanges = []
    with open("day2.txt") as productIds:
        ranges = productIds.read().split(",")
        for idRange in ranges:
            start, end = map(int, idRange.split("-"))
            idRanges.append((start, end))
    
    invalid = 0

    for start, end in idRanges:
        for id in range(start, end+1):
            if findInvalid(id):
                invalid += id
    
    print("Part 1:", invalid)

    invalid = 0

    for start, end in idRanges:
        for id in range(start, end+1):
            if findAllInvalid(id):
                invalid += id
    
    print("Part 2", invalid)

if __name__=="__main__":
    main()
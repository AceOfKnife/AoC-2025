def backtrack(visited, current, devices, memo):
    if current == "out":
        return 1
    
    visited.add(current)

    if current not in memo:
        paths = 0
        for output in devices[current]:
            if output in visited:
                continue
            paths += backtrack(visited, output, devices, memo)
        memo[current] = paths
    visited.remove(current)
    return memo[current]

def backtrack2(current, devices, visited, foundDAC, foundFFT, memo):
    key = (current, foundDAC, foundFFT)

    if key in memo:
        return memo[key]

    if current == "out":
        memo[key] = 1 if (foundDAC and foundFFT) else 0
        return memo[key]

    visited.add(current)

    if current == "dac":
        foundDAC = True
    elif current == "fft":
        foundFFT = True

    paths = 0
    for output in devices[current]:
        if output in visited:
            continue
        paths += backtrack2(output, devices, visited, foundDAC, foundFFT, memo)

    visited.remove(current)
    memo[key] = paths
    return paths



def main():

    devices = {}
    with open("day11.txt") as devicesAndOutputs:
        for line in devicesAndOutputs:
            i = 0
            while line[i] != ':':
                i += 1
            device = line[:i]
            i += 2
            outputs = line[i:].replace("\n", "").split(" ")
            devices[device] = outputs
    print("Part 1:", backtrack(set(), "you", devices, {}))

    print("Part 2:", backtrack2("svr", devices, set(), False, False, {}))
    
if __name__=="__main__":
    main()
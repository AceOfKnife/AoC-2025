from collections import deque
import numpy as np

def pushButton(state, button):
    newState = list(state)
    for press in button:
        newState[press] = 0 if newState[press] == 1 else 1
    return tuple(newState)

def main():

    finalStates = []
    buttons = []
    joltStates = []
    with open("day10.txt") as manualInput:
        for line in manualInput:

            words = line.replace("\n", "").split(" ")
            state = []
            for i in range(1, len(words[0]) - 1):
                if words[0][i] == '.':
                    state.append(0)
                else:
                    state.append(1)
            finalStates.append(tuple(state))

            buttonChoices = []
            for i in range(1, len(words) - 1):
                button = words[i][1:len(words[i])-1]
                buttonChoices.append(tuple(map(int, button.split(","))))
            buttons.append(tuple(buttonChoices))
            joltStates.append(tuple(map(int, words[-1][1:len(words[-1])-1].split(","))))
    
    fewestButtons = 0

    for finalState, buttonChoices in zip(finalStates, buttons):
        startingState = tuple([0] * len(finalState))
        q = deque([startingState])
        buttonPresses = 0
        found = False
        seen = set(startingState)

        while q:
            for _ in range(len(q)):
                currentState = q.popleft()
                if currentState == finalState:
                    found = True
                    break

                for button in buttonChoices:
                    newState = pushButton(currentState, button)
                    if newState not in seen:
                        seen.add(newState)
                        q.append(newState)

            if found:
                break
            buttonPresses += 1
        fewestButtons += buttonPresses

    print("Part 1:", fewestButtons)

    
if __name__=="__main__":
    main()
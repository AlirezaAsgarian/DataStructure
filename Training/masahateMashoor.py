def calculateLeftIndex(indexOfRectangleHeight, leftStack, rectangleHeights):
    if len(leftStack) == 0:
        leftStack.append(indexOfRectangleHeight)
        return -1

    while len(leftStack) != 0 and rectangleHeights[indexOfRectangleHeight] <= rectangleHeights[leftStack[-1]] :
        leftStack.pop()
    result = 0
    if len(leftStack) == 0 : result = -1
    else: result = leftStack[-1]
    leftStack.append(indexOfRectangleHeight)
    return result


def calculateMaxAccordingToRightIndexAndLeftIndexes(indexOfRectangleHeight, rectangleHeights, rightsStack, lefts):
    if len(rightsStack) == 0:
        rightsStack.append(indexOfRectangleHeight)
        return rectangleHeights[indexOfRectangleHeight] * (len(rectangleHeights) - lefts[indexOfRectangleHeight] - 1)

    while len(rightsStack) != 0 and rectangleHeights[indexOfRectangleHeight] <= rectangleHeights[rightsStack  [-1]] :
        rightsStack.pop()
    rightIndex = 0
    if len(rightsStack) == 0 : rightIndex = len(rectangleHeights)
    else: rightIndex = rightsStack[-1]
    rightsStack.append(indexOfRectangleHeight)
    return rectangleHeights[indexOfRectangleHeight] * (rightIndex - lefts[indexOfRectangleHeight] -1)


def printResult(rectangleHeights):
    numberOfRectangle = len(rectangleHeights)
    lefts = [0] * numberOfRectangle
    leftsStack = []
    rightsStack = []
    maxArea = 0
    for indexOfRectangleHeight in range(0, numberOfRectangle, 1):
        lefts[indexOfRectangleHeight] = calculateLeftIndex(indexOfRectangleHeight, leftsStack, rectangleHeights)
    for indexOfRectangleHeight in range(numberOfRectangle - 1, -1, -1):
        currentRectangleHeightMaxArea = calculateMaxAccordingToRightIndexAndLeftIndexes(indexOfRectangleHeight,
                                                                                        rectangleHeights, rightsStack,
                                                                                        lefts)
        maxArea = currentRectangleHeightMaxArea if (currentRectangleHeightMaxArea > maxArea) else maxArea
    print(maxArea)


numberOfRectangles = int(input())
rectangleHeights = [0] * numberOfRectangles

rectangleInputs = input()
for height in rectangleInputs.split():
    rectangleHeights.append(int(height))

printResult(rectangleHeights)

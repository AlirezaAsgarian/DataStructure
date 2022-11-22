

def print_hi(name):
    return "Ali"  # Press Ctrl+F8 to toggle the breakpoint.


def formatted_name(first_name, last_name, middle_name=''):
    if len(middle_name) > 0:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


def merge(rightArray, leftArray):
    rightIndex = 0
    leftIndex = 0
    result = []
    leftIndex, rightIndex = add_elements_to_result_until_one_array_finished(leftArray, leftIndex, result, rightArray, rightIndex)
    addRemainElementsToResult(leftArray, leftIndex, result, rightArray, rightIndex)
    return result


def add_elements_to_result_until_one_array_finished(leftArray, leftIndex, result, rightArray, rightIndex):
    while isOneArrayFinished(leftArray, leftIndex, rightArray, rightIndex):
        leftIndex, rightIndex = addElements(leftArray, leftIndex, result, rightArray, rightIndex)
    return leftIndex, rightIndex


def isOneArrayFinished(leftArray, leftIndex, rightArray, rightIndex):
    return rightIndex < len(rightArray) and leftIndex < len(leftArray)


def addElements(leftArray, leftIndex, result, rightArray, rightIndex):
    if rightArray[rightIndex] < leftArray[leftIndex]:
        rightIndex = appendElementOfRightArrayToResult(result, rightArray, rightIndex)
    else:
        result.append(leftArray[leftIndex])
        leftIndex += 1
    return leftIndex, rightIndex


def addRemainElementsToResult(leftArray, leftIndex, result, rightArray, rightIndex):
    if leftIndex == len(leftArray):
        while rightIndex < len(rightArray):
            result.append(rightArray[rightIndex])
            rightIndex += 1
    else:
        while leftIndex != len(leftArray):
            result.append(leftArray[leftIndex])
            leftIndex += 1


def appendElementOfRightArrayToResult(result, rightArray, rightIndex):
    result.append(rightArray[rightIndex])
    rightIndex += 1
    return rightIndex


def merge_sort(array) :
    if len(array) == 1: return list(array)
    middle = len(array) // 2
    return merge(merge_sort(array[middle:]),merge_sort(array[:middle]))
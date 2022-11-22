
def number_of_halat(value) :
    k = 2
    result = 0
    while True :
        cube = k**3
        if cube > value : break
        result += (value // cube)
        k += 1
    return result


def binary_search(target, left, right):
    if left < right : return -1
    currentValue = (left + right) // 2
    #  print("%d %d %d" % (currentValue , left , right))
    number_of_halats = number_of_halat(currentValue)
    if target == number_of_halats:
        return currentValue
    if target > number_of_halats:
        return binary_search(target, left, currentValue + 1)
    if target < number_of_halats:
        return binary_search(target, currentValue - 1, right)


def getResult(value):
    result = binary_search(value, 10 ** 15 , 0)
    halatCurrentResult = number_of_halat(result)
    if result == -1:
        return result
    while halatCurrentResult == number_of_halat(result - 1):
        result -= 1
    return result


#n = int(input())
#print(getResult(n))

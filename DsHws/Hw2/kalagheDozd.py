import math



def getAppropiateNumbers(numbers):
    outputPrimes = []
    maxSizeOfArray = 16 * numbers
    primes = [True] * maxSizeOfArray
    counter = 0
    currentNumber = 2
    sqrtOfMaxSize = int(math.sqrt(maxSizeOfArray))
    for i in range(2, sqrtOfMaxSize):
        if primes[i]:
                powerOfTwoDivision = i * i
                for j in range(i * i, maxSizeOfArray, i):
                    if powerOfTwoDivision != j :
                        primes[j] = False
                    else:
                        powerOfTwoDivision *= powerOfTwoDivision
    for i in range(2, maxSizeOfArray):
        if primes[i]:
            counter += 1
            outputPrimes.append(i)
        if counter == numbers : break

    return outputPrimes




def printResult(inputSerial):
    prime_numbers = getAppropiateNumbers(inputSerial)
    result = 1
    for i in range(0,inputSerial) :
        result *= prime_numbers[i]
        if result > 1000000007 : result %= 1000000007
    print(result)

serial = int(input())
printResult(serial)

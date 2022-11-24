import math


class heap:
    primes = None

    def __init__(self, primes):
        self.primes = primes

    def removeMin(self):
        min = self.primes[0]
        self.primes[0] = self.primes[len(self.primes) - 1]
        self.primes.pop(len(self.primes) - 1)
        self.min_heapify_down(0)
        return min

    def min_heapify_down(self, i):
        left = self.getLeftChildren(i)
        right = self.getRightChildren(i)
        smallest = i
        if left < len(self.primes) and self.primes[left] < self.primes[i]:
            smallest = left
        if right < len(self.primes) and self.primes[right] < self.primes[smallest]:
            smallest = right
        if smallest != i:
            self.primes[smallest], self.primes[i] = self.primes[i], self.primes[smallest]
            self.min_heapify_down(smallest)

    def getLeftChildren(self, i):
        return 2 * i

    def getRightChildren(self, i):
        return 2 * i + 1

    def push(self, insertedNumber):
        self.primes.append(insertedNumber)
        self.min_heapify_up(len(self.primes) - 1)

    def min_heapify_up(self, input):
        if input == 0: return
        if self.primes[input] < self.primes[self.parent(input)]:
            self.primes[input], self.primes[self.parent(input)] = self.primes[self.parent(input)], self.primes[input]
            self.min_heapify_up(self.parent(input))

    def parent(self, input):
        return int(input / 2)
def isPrime(x):
    for i in range(2, x):
        if x % i == 0: return False
    return True




def getPrimeNumbers(primeNumbers):
    output_primes = []
    primes = [True] * (16000000)
    counter = 0
    currentNumber = 2
    for i in range(2, 16000000):
        if primes[i]:
            output_primes.append(i)
            if len(output_primes) == primeNumbers: break
            if i * i < 16000000:
                for j in range(i, 16000000, i):
                    primes[j] = False
    return output_primes


def LogN(n, x):
    return (math.log10(x) / math.log10(n))


def isPowerOfTwo(n):
    return (math.ceil(LogN(2, n)) == math.floor(LogN(2, n)))


def isPowerOfN(n, x):
    return (math.ceil(LogN(n, x)) == math.floor(LogN(n, x)))


def isDivisionOfPowerOfTwo(base, value):
    if isPowerOfN(base, value):
        if isPowerOfTwo(LogN(base, value)):
            return True
        else:
            return False
    else:
        return False




def getAppropiateNumbers(numbers):
    outputPrimes = []
    maxSizeOfArray = 16 * numbers
    primes = [True] * maxSizeOfArray
    counter = 0
    currentNumber = 2
    sqrtOfMaxSize = int(math.sqrt(maxSizeOfArray))
    for i in range(2, sqrtOfMaxSize):
        if primes[i]:
                ddr = i * i
                for j in range(i * i, maxSizeOfArray, i):
                    if ddr != j :
                        primes[j] = False
                    else:
                        ddr *= ddr
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

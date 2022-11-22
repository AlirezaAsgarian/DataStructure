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


def printResult(inputSerial):
    prime_numbers = getPrimeNumbers(inputSerial)
    minHeap = heap(prime_numbers)
    currentserial = 0
    result = 1
    while currentserial != inputSerial:
        min_prime = minHeap.removeMin()
        result *= min_prime
        result %= 1000000007
        min_prime = min_prime ** 2
        currentserial += 1
        minHeap.push(min_prime)
    print(result)



serial = int(input())
printResult(serial)

class node:
    def __init__(self, key, value, isRight):
        self.key = key
        self.value = value
        self.isRight = isRight


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i].key <= R[j].key:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)


def is_left_len_smaller(leftLen, rightLen):
    return leftLen < rightLen


right = list()
left = list()
total = list()
totalCopy = list()
lenRight = 0
lenLeft = 0

numberOfLines = int(input())

for i in map(int, input().split()):
    n = node(i, 0, True)
    total.append(n)
    totalCopy.append(n)

merge_sort(totalCopy, 0, len(total) - 1)
rightSum = 0
leftSum = 0
for i in totalCopy:
    if lenRight > lenLeft:
        left.append(i)
        leftSum += lenLeft
        lenLeft += i.key
        i.value = -lenLeft
    else:
        right.append(i)
        rightSum += lenRight
        lenRight += i.key
        i.value = lenRight - i.key


print("%.7f" % ((leftSum + rightSum) / numberOfLines))

for i in total:
    print(i.value, end=" ")

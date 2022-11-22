



def getResult(input) :
    resultStack = []
    for i in input :
        if i == '=':
           if len(resultStack) != 0 :
            resultStack.pop()
        else: resultStack.append(i)
    for i in resultStack :
        print(i , end="")



getResult(input())
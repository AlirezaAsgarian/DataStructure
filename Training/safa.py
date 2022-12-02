
from collections import deque


def print_result(number_of_queue, number_of_instructions, instructions):
    queues = [0] * number_of_queue
    mainList = list()
    executeInstructions(number_of_instructions, instructions, queues, mainList)


def executeFirstTypeOfInstruction(value,mainList):
    if len(mainList) == 0 :
             mainList.append(value)
    else:
        mainList.append(mainList[-1] + value)



def executeSecondTypeOfInstruction(queue,index_of_queue,number_of_exiting_values,mainList):
    result = 0
    if queue[index_of_queue - 1] != 0 :
        result += mainList[queue[index_of_queue - 1] - 1]
    queue[index_of_queue - 1] += number_of_exiting_values
    result = mainList[queue[index_of_queue - 1] - 1] - result
    print(result)

def executeInstructions(number_of_instructions,instructions,queues,mainList):
    for i in range(number_of_instructions):
        executeInstruction(instructions.popleft(),queues,mainList)


def createQueues(number_of_queue):
    queues = []
    for i in range(number_of_queue):
        queues.append(deque())
    return  queues



def executeInstruction(instruction , queues , mainList):
    splitedInstruction = instruction.split()
    if len(splitedInstruction) == 2 :
        executeFirstTypeOfInstruction(value=int(splitedInstruction[1]),mainList=mainList)
    else:
        executeSecondTypeOfInstruction(queue=queues ,index_of_queue=int(splitedInstruction[1])
                                       ,number_of_exiting_values=int(splitedInstruction[2]),mainList=mainList)



# number_of_queues_and_instructions = input()
# number_of_queues = int(number_of_queues_and_instructions.split()[0])
# number_of_instructions = int(number_of_queues_and_instructions.split()[1])
# queue_of_instructions = deque()
# queues = [0] * number_of_queues
# mainList = list()
# for i in range(number_of_instructions) :
#     splitedInstruction = input().split()
#     if len(splitedInstruction) == 2:
#         executeFirstTypeOfInstruction(value=int(splitedInstruction[1]), mainList=mainList)
#     else:
#         executeSecondTypeOfInstruction(queue=queues, index_of_queue=int(splitedInstruction[1])
#                                        , number_of_exiting_values=int(splitedInstruction[2]), mainList=mainList)
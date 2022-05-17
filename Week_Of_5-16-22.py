from collections import deque
from typing import TypeVar
from collections import *

_T = TypeVar("_T")


def SumLists(list1: list, list2: list, reversed: bool = True):
    longest: list
    shortest: list
    num1 = 0
    num2 = 0
    # Assigns the shortest and longest lists in case they are different lengths
    # Also changes them to forward order if needed
    if len(list1) > len(list2):
        if reversed:
            longest = list(list1.__reversed__())
            shortest = list(list2.__reversed__())
        else:
            longest = list1
            shortest = list2
    else:
        if reversed:
            longest = list(list2.__reversed__())
            shortest = list(list1.__reversed__())
        else:
            longest = list2
            shortest = list1
    # For each list the total number is multiplied by 10 then the current number is added to it
    # ie if the current total is 4 and the next number to add is 7: 4 * 10 = 40; 40 + 7 = 47
    for x in range(len(longest)):
        if x < len(shortest):
            num1 *= 10
            num1 += shortest[x]
        num2 *= 10
        num2 += longest[x]
    resultList = []
    # Adds them together and casts to a string
    result = str(num1 + num2)
    # Appends the current character to the resultList after being cast back to int
    for x in result:
        resultList.append(int(x))
    return resultList


class Stack(deque):
    # Secondary stack for tracking the minimum value
    # Appends to the left so the smallest value is always at 0
    _min = deque()

    def append(self, x: _T) -> None:
        # Appends value to min if it's the first element added
        if len(self._min) == 0:
            self._min.append(x)
        elif x <= self._min[0]:
            self._min.appendleft(x)
        super().append(x)
    # If the popped value equals the current minimum it is removed from min as well
    # Because its FILO they will always be removed in the correct order
    def pop(self):
        if self._min[0] == self[len(self) - 1]:
            self._min.popleft()
        super().pop()
    # Returns the current minimum
    def min(self):
        return self._min[0]


def StackDemo():
    print()
    print('--Stack Min Demo--')
    stack = Stack()
    stack.append(5)
    stack.append(4)
    stack.append(25)
    stack.append(2)
    print(stack)
    print('Min: ' + stack.min().__str__())
    stack.pop()
    print(stack)
    print('Min: ' + stack.min().__str__())
    stack.pop()
    print(stack)
    print('Min: ' + stack.min().__str__())
    stack.pop()
    print(stack)
    print('Min: ' + stack.min().__str__())


def SumDemo():
    print()
    print('--Sum Lists Demo--')
    list1 = [7, 1, 6]
    list2 = [5, 9, 2]
    print('Stored in reverse order: ')
    print('list 1: ' + list1.__str__())
    print('list 2: ' + list2.__str__())
    print('result: ' + SumLists(list1, list2).__str__())
    list1 = [6, 1, 7]
    list2 = [2, 9, 5]
    print('Stored in forward order: ')
    print('list 1: ' + list1.__str__())
    print('list 2: ' + list2.__str__())
    print('result: ' + SumLists(list1, list2, False).__str__())


SumDemo()
StackDemo()

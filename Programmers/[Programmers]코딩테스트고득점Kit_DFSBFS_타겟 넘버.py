# sol1
def solution(numbers, target):
    stack = [0]
    for number in numbers:
        temp = []
        for s in stack:
            temp.append(s + number)
            temp.append(s - number)
        stack = temp

    return temp.count(target)

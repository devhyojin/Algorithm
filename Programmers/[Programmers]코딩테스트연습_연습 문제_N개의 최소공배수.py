def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return (x * y) // gcd(x, y)


def solution(arr):
    temp = arr[:]
    while len(temp) != 1:
        result = []
        for i in range(0, len(temp) // 2):
            result.append(lcm(temp[2 * i], temp[2 * i + 1]))
        if len(temp) % 2:
            result.append(arr[-1])
        temp = result
    return temp[0]
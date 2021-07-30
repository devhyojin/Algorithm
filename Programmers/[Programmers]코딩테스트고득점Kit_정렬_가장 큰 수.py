def solution(numbers):
    numbers = sorted(list(map(str, numbers)), key=lambda x: x*3)[::-1]
    if numbers.count('0') == len(numbers):
        return '0'
    return ''.join(numbers)
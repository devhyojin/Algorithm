def solution(price, money, count):
    spend = (count*(count+1)//2)*price
    answer = spend-money
    if money >= spend:
        return 0
    else:
        return answer
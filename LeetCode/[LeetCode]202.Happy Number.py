#sol1
class Solution:
    def isHappy(self, n: int) -> bool:

        while n ** 2 >= 10:
            new_num = 0
            while n > 0:
                temp = (n % 10) ** 2
                new_num += temp
                n //= 10
            n = new_num
        if n == 1:
            return True
        else:
            return False
```
시간초과 걸려버린 풀이었다. 너무 느린 방법으로 푼 것 같았다.
사실 무한반복하면 1이 되지 않는다는 부분을 잘못 해석해서 좀 현명하지 않은 방법으로 풀어서 문제가 된 것 같다.
```

#sol2
class Solution:
    def isHappy(self, n: int) -> bool:
        cycle = set()
        while n not in cycle:
            cycle.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
        return n == 1
```
반복되는 결과가 나오는지 체크하기 위해서 계산 값을 계속 cycle에 추가해서 살폈다.
32ms 14.2MB로 마무리했다.
```
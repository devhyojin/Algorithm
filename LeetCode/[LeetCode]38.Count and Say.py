#sol1
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        digit_s = self.countAndSay(n - 1)
        i, char, answer = 0, digit_s[0], ''

        for j in range(1, len(digit_s)):
            if digit_s[j] != char:
                answer += str(j - i) + char
                i, char = j, digit_s[j]
        answer += str(len(digit_s) - i) + char
        return answer
```
숫자가 연속하지 않은 경우에는 바로 answer에 더해주는 방식으로 구현했다.
44ms 14.3MB 라는 결과가 나왔다.
```

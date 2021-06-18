#sol1
class Solution:
    def romanToInt(self, s: str) -> int:
        sym_dic = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
        answer = 0
        for i in range(len(s)-1):
            if sym_dic[s[i]] >= sym_dic[s[i+1]]:
                print(type(sym_dic[s[i]]))
                answer += sym_dic[s[i]]
            else:
                answer -= sym_dic[s[i]]
        return answer + sym_dic[s[-1]]
```
단순하게, for문을 돌았다. 64ms 14.2MB가 사용되어 코드를 조금 더 개선해보고자
노력했다
```

#sol2
class Solution:
    def romanToInt(self, s: str) -> int:
        sym_dic = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
        prev, answer = 0, 0
        for i in s[::-1]:
            A = sym_dic[i]
            if prev <= A:
                answer += A
            else:
                answer -= A
            prev = A
        return answer
```
인덱스를 구하는 작업에 시간을 쏟지 않으려 했다. 결과는 44ms 14.2MB였다
```

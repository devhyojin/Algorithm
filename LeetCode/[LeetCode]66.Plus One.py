#sol1
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = int(''.join(list(map(str, digits)))) + 1
        temp = str(temp)
        return [int(temp[i]) for i in range(len(temp))]
```
24ms 14.4MB
```
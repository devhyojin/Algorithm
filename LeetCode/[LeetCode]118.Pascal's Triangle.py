# sol1
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = [[1]*(i+1) for i in range(numRows)]
        for j in range(2, numRows):
            for k in range(1, j):
                answer[j][k] = answer[j-1][k-1] + answer[j-1][k]
        return answer
```
무작정 1을 다 채워넣고, 인덱스가 0이거나 -1이 아닌 곳에 대하여 값을 갱신했다.
```

#sol2
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []
        for i in range(numRows):
            # The first and last row elements are always 1.
            row = [None for _ in range(i + 1)]
            row[0], row[-1] = 1, 1
            for j in range(1, len(row) - 1):
                row[j] = answer[i - 1][j - 1] + answer[i - 1][j]
            answer.append(row)
        return answer
```
행의 머리와 꼬리에만 1을 채워넣고 그 안의 부분의 값을 계산하여 넣었다.
```

#sol1
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        for i in nums1:
            if i in nums2:
                nums2.remove(i)
                answer.append(i)
        return answer
```
68ms 14.3MB가 나왔다.
```

#sol2
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = list((Counter(nums1) & Counter(nums2)).elements())
        return answer
```
Counter라는 것을 찾아서 한 번 적용해보았다. 시간 복잡도는 O(n)이다.
40ms 14.5MB
```

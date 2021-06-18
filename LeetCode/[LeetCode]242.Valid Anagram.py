# sol1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        leng = len(s)
        if leng != len(t):
            return False
        for i in range(leng):
            temp = s[i]
            idx = t.find(temp)
            if idx > -1:
                t = t[:idx] + t[idx+1:]
        if t:
            return False
        else:
            return True
# 생각나는대로 구현했지만 904초라는 엄청난 시간이 걸렸다....

#sol2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic, t_dic = {}, {}
        for alphabet in s:
            s_dic[alphabet] = s_dic.get(alphabet, 0) + 1
        for check in t:
            t_dic[check] = t_dic.get(check, 0) + 1
        if s_dic == t_dic:
            return True
        else:
            return False
#딕셔너리로 구성 알파벳들을 정리해 비교하는 식으로 풀어보았다.

#sol3
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False
#.sort()와 sorted() 모두 시간 복잡도가 NlogN인데, .sort()는 런타임에러가 났다. 검색해봤더니 .sort()는 오로지 list에서만 사용 가능한 함수라고 한다. 잊지 말자.

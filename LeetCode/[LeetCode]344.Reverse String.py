#sol1
class Solution:
    def reverseString(self, s):
        s[:] = s[::-1]


#sol2
class Solution:
    def reverseString(self, s):
        s.reserve()

#sol3
class Solution:
    def reverseString(self, s):
        for i in range(len(s)//2):
            s[i], s[-i-1] = s[-i-1], s[i]
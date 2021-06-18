class Solution:

    def maxDepth(self, root: TreeNode) -> int:
        if root:

            def equation(n):
                answer = (2*(n**3)-3*(n**2)+n+6)//6
                return answer
            
            rool = [root]
            leng = len(rool)
            a = 1 
            while leng - equation(a) > 0:
                a + = 1               
            return a
        else:
            return  0

# 저 왜 틀렸나요..  뭐 잘못했나요
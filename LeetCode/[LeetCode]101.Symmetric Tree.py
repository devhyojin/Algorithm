#sol 1
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(L, R):
            if not L and not R:
                return True
            if L and R and L.val == R.val:
                return isMirror(L.left, R.right) and isMirror(L.right, R.left)
            return False
        return isMirror(root, root)
    ```
    대칭트리인지 확인한 후 아니면 False값을 반환하고
    대칭트리이면, 거울 모드인지 계속해서 확인해서 값을 반환한다.
    ```
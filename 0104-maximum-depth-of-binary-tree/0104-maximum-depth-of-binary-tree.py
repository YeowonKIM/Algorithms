# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        if root is None:
            return max_depth;
        q = deque()
        q.append((root, 1))
        while q:
            curr_node, curr_depth = q.popleft()
            max_depth = max(max_depth, curr_depth)
            if curr_node.left:
                q.append((curr_node.left, curr_depth+1))
            if curr_node.right:
                q.append((curr_node.right, curr_depth+1))
        return max_depth
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre = 0
        indices =  {v:i for i,v in enumerate(inorder)}
        def dfs(l,r):
            nonlocal pre 
            if l>r:
                return 
            node = TreeNode()
            node.val = preorder[pre]
            mid = indices[node.val]
            pre+=1
            node.left = dfs(l, mid-1)
            node.right = dfs(mid+1, r)
            return node


        return dfs(0, len(inorder)-1)



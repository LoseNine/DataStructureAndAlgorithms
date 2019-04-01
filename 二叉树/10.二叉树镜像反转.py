def reversed(root):
    if root==None:
        return
    reversed(root.left)
    reversed(root.right)
    tmp=root.left
    root.left=root.right
    root.right=tmp
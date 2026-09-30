from collections import deque

def maxDepth(root):
    if root is None:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)

    return 1+max(left_depth, right_depth)

def isBalanced(root):
    if root is None:
        return True

    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)

    if abs(left_depth - right_depth)>1:
        return False

    return isBalanced(root.right) and isBalanced(root.left)

def diameterOfBinaryTree(root):
    diameter = 0

    def depth(node):
        nonlocal diameter

        if node is None:
            return 0
        left_depth = depth(node.left)
        right_depth = depth(node.right)
        diameter = max(diameter, left_depth+right_depth)

        return 1+max(left_depth, right_depth)

    depth(root)
    return diameter
    
def isSameTree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False

    left_same = isSameTree(p.left, q.left)
    right_same = isSameTree(p.right, q.right)

    return left_same and right_same

def invertTree(root):
    if root is None:
        return None

    root.left, root.right = root.right, root.left

    invertTree(root.left)
    invertTree(root.right)

    return root

def levelOrder(root):
    if root is None:
        return []
    queue = deque([root])
    result = []

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        result.append(level)

    return result

def hasPathSum(root, targetsum):
    if root is None:
        return False
    if root.left is None and root.right is None:
        return root.val == targetsum

    remianing_sum = targetsum - root.val
    return hasPathSum(root.left, remianing_sum) or hasPathSum(root.right, remianing_sum)

def isMirror(t1, t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    if t1.val != t2.val:
        return False

    return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

def isSymmetric(root):
    if root is None:
        return True

    return isMirror(root.left, root.right)

def isSubtree(root, subRoot):
    if root is None:
        return False
    if isSameTree(root, subRoot):
        return True

    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)

def lowestCommonAncestor(root, p, q):
    if root is None:
        return None
    if root is p or root is q:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left is not None and right is not None:
        return root
    if left is not None:
        return left
    return right

def searchBST(root, val):
    if root is None:
        return None
    if root.val == val:
        return root
    if root.val > val:
        return searchBST(root.left, val)
    if root.val < val:
        return searchBST(root.right, val)

def check(node, low, high):
    if node is None:
        return True
    if node.val <= low or node.val >= high:
        return False
    return check(node.left, low, node.val) and check(node.right, node.val, high)

def isValidBST(root):
    if root is None:
        return True
    return check(root, float('-inf'), float('inf'))

def kthSmallest(root, k):
    values = []

    def inorder(node):
        if node is None:
            return

        inorder(node.left)
        values.append(node.val)
        inorder(node.right)

    inorder(root)
    return values[k-1]

def lowestCommonAncestorBST(root, p, q):
    if root is None:
        return None

    if p.val < root.val and q.val < root.val:
        return lowestCommonAncestorBST(root.left, p, q)
    elif p.val > root.val and q.val > root.val:
        return lowestCommonAncestorBST(root.right, p, q)
    else:
        return root

def insertIntoBST(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insertIntoBST(root.left, val)
    if val > root.val:
        root.right = insertIntoBST(root.right, val)
    return root

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_val = preorder.pop(0)
    index = inorder.index(root_val)
    root = TreeNode(root_val)

    root.left = buildTree(preorder, inorder[:index])
    root.right = buildTree(preorder, inorder[index + 1:])

    return root

def buildTree(preorder, inorder):
    positions = {value: index for index, value in enumerate(inorder)}
    preorder_index = 0

    def build(left, right):
        nonlocal preorder_index
        if left > right:
            return None

        root_val = preorder[preorder_index]
        preorder_index += 1
        root = TreeNode(root_val)

        root.left = build(left, positions[root_val] - 1)
        root.right = build(positions[root_val] + 1, right)

        return root
    
    return build(0, len(inorder) - 1)

def deleteNode(root, key):
    if root is None:
        return None
    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            successor = root.right
            while successor.left:
                successor = successor.left
            root.val = successor.val
            root.right = deleteNode(root.right, successor.val)
    return root

def buildTree(preorder, inorder):
    position = {value: index for index, value in enumerate(inorder)}
    preorder_index = 0

    def build(left, right):
        nonlocal preorder_index
        if left > right:
            return None

        root_val = preorder[preorder_index]
        preorder_index += 1
        root = TreeNode(root_val)

        root.left = build(left, position[root_val]-1)
        root.right = build(position[root_val]+1, right)

        return root
    return build(0, len(inorder)-1)

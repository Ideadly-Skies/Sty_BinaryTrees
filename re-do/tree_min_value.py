class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# def tree_min_value(root, min_val=float("inf")):
#     # base case
#     if root is None:
#         return min_val

#     # update min_val
#     min_val = min(root.val, min_val)

#     # recursive case
#     left_res = tree_min_value(root.left, min_val)
#     right_res = tree_min_value(root.right, min_val)

#     # return the minimum out of the two subtree
#     return min(left_res, right_res)

def tree_min_value(root):
    # guard against edge cases 
    if root is None:
        return float("inf")

    # base case
    if root.left is None and root.right is None:
       return root.val

    # recursive case
    left_res = tree_min_value(root.left)
    right_res = tree_min_value(root.right)

    # find minimum number
    return min(root.val, left_res, right_res)

if __name__ == "__main__":
    a = Node(3)
    b = Node(11)
    c = Node(4)
    d = Node(4)
    e = Node(-2)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #       3
    #    /    \
    #   11     4
    #  / \      \
    # 4   -2     1
    print(tree_min_value(a)) # -> -2

    a = Node(5)
    b = Node(11)
    c = Node(3)
    d = Node(4)
    e = Node(14)
    f = Node(12)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #       5
    #    /    \
    #   11     3
    #  / \      \
    # 4   14     12

    print(tree_min_value(a)) # -> 3
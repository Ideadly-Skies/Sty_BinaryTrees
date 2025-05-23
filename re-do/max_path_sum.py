class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


"""
==================================================

        Correct Case (Refined Approach)

==================================================
"""
def max_path_sum(root):
    # guard againt edge case 
    if root is None:
        return float("-inf")
    
    # base case
    if root.left is None and root.right is None:
       return root.val

    # recursive case
    left_child = max_path_sum(root.left)
    right_child = max_path_sum(root.right)
    max_child = max(left_child, right_child)

    # maximum
    return root.val + max_child

"""
==================================================

        Incorrect Case (Original Approach)

==================================================
"""
def max_path_sum(root, max_sum=float("-inf"), total=0):
    # base case 
    if root is None:
        max_sum = max(max_sum, total)
        return max_sum

    # update running total
    total += root.val

    # recursive case
    left_res = max_path_sum(root.left, max_sum, total)
    right_res = max_path_sum(root.right, max_sum, total)

    # output maximum child
    return max(left_res, right_res)

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

    print(max_path_sum(a)) # -> 18

    a = Node(5)
    b = Node(11)
    c = Node(54)
    d = Node(20)
    e = Node(15)
    f = Node(1)
    g = Node(3)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    e.left = f
    e.right = g

    #        5
    #     /    \
    #    11    54
    #  /   \      
    # 20   15
    #      / \
    #     1  3

    print(max_path_sum(a)) # -> 59

    a = Node(-1)
    b = Node(-6)
    c = Node(-5)
    d = Node(-3)
    e = Node(0)
    f = Node(-13)
    g = Node(-1)
    h = Node(-2)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h

    #        -1
    #      /   \
    #    -6    -5
    #   /  \     \
    # -3   0    -13
    #     /       \
    #    -1       -2

    print(max_path_sum(a)) # -> -8

    a = Node(42)

    #        42

    print(max_path_sum(a)) # -> 42
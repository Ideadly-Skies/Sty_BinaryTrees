"""
=======================================
        Iterative Solution
=======================================
"""
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

# def depth_first_values(root):
#     if root is None:
#        return [] 

#     # init stack with root 
#     stack = [root]

#     # values to store traversed nodes
#     values = []
#     while stack:
#         curr = stack.pop()
#         values.append(curr.val) 
        
#         if curr.right:
#             stack.append(curr.right)
#         if curr.left:
#             stack.append(curr.left)

#     # return values traversed
#     return values

"""
=======================================
        Recursive Solution
=======================================
"""
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def depth_first_values(root):
    # base case stop here 
    if root is None:
       return [] 

    # visit subtrees 
    left_subtree = depth_first_values(root.left)    # [b, d, e] 
    right_subtree = depth_first_values(root.right)  # [c, f]

    # return value
    return [root.val, *left_subtree, *right_subtree]

# a -> [a, [b, [d, [], []], [e, [], []]], ]
# b -> [b, [d, [], []], [e, [], []]]
# d -> [d, [], []]
# e -> [e, [], []]

# right traversal
# a -> [a, [b, [d, [], []], [e, [], []]], [c, [], [f, [], []]]]
# c -> [c, [], [f, [], []]]
# f -> [f, [], []]

if __name__ == "__main__":
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')        
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f

    values = depth_first_values(a)
    #   -> ['a', 'b', 'd', 'e', 'c', 'f']

    print(values)
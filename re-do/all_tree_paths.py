class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def all_tree_paths(root):
    # get all the result 
    results = _all_tree_paths(root)
    
    for sub_list in results:
        sub_list.reverse()

    # return results
    return results 

def _all_tree_paths(root):
    # base case
    if root is None:
        return []

    # return the leaf node
    if (root.left is None and root.right is None):
        return [[root.val]]

    # all_paths store all the paths in a binary tree
    all_paths = []

    # recurse down the left subpaths
    left_subpaths = _all_tree_paths(root.left)
    for path in left_subpaths:
        path.append(root.val)
        all_paths.append(path)

    # recurse down the right subpaths
    right_subpaths = _all_tree_paths(root.right)
    for path in right_subpaths:
        path.append(root.val)
        all_paths.append(path)

    # return all_paths
    return all_paths

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

    print(all_tree_paths(a)) # ->
    # [ 
    #   [ 'a', 'b', 'd' ], 
    #   [ 'a', 'b', 'e' ], 
    #   [ 'a', 'c', 'f' ] 
    # ] 
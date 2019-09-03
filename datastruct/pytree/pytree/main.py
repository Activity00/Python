from datastruct.pytree.pytree import BiTree
from datastruct.pytree.pytree.tree import BSTree
from datastruct.pytree.pytree.utils import print_tree

if __name__ == '__main__':
    tree_list = [15, 6, 18, 3, 7, 17, 20, 2, 4, None, 13, None, None, None, None, None, None, None, None, 9, None]
    bstree = BSTree.build_from_list(tree_list)
    print_tree(bstree)
    print(bstree.search(13))

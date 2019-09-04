from datastruct.pytree.pytree.tree import BSTree, BitNode
from datastruct.pytree.pytree.utils import print_tree

if __name__ == '__main__':
    # tree_list = [15, 6, 18, 3, 7, 17, 20, 2, 4, None, 13, None, None, None, 22, None, None, None, None, None, None, 9,
    #             None, None, None, None, None, None, None, None, 23]
    tree_list = [15, 6, 18, 3, 7, 17, 20, 2, 4, None, 13, None, None, None,None, None, None, None, None, None, None, 9,
                 None]
    bstree = BSTree.build_from_list(tree_list)
    print_tree(bstree)
    bstree.transplant(bstree.search(15), bstree.search(7))
    print_tree(bstree)

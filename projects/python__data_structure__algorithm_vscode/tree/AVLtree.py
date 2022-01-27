from bst import BiTreeNode, BST

class AVLNode(BiTreeNode):  # 继承
    def __init__(self, data):
        BiTreeNode.__init__(self, data)
        self.bf = 0  # 平衡因子 此处为右减左

class AVLTree(BST):
    def __init__(self, li=None):
        BST.__init__(self, li)

    def rotate_left(self, p, c):  # 右孩子的右子树插入 左旋 两个节点 p祖先 c右孩子
        s2= c.lchild  # 右孩子的左子树
        p.rchild = s2  # 把右孩子换成右孩子的左子树
        if s2:  # s2不为空
            s2.parent = p  # 右孩子的左子树的祖先是p
            
        c.lchild = p  # c的左孩子变成祖先p
        p.parent = c  # p的祖先变成原本的右孩子c

        p.bf = 0  # 平衡因子
        c.bf = 0
        return c

    def rotate_right(self, p, c):  # 左孩子的左子树插入 左旋
        s2 = c.rchild
        p.lchild = s2
        if s2:
            s2.parent = p
            
        c.rchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0
        return c

    def rotate_right_left(self, p, c):
        g = c.lchild

        s3 = g.rchild
        c.lchild = s3
        if s3:
            s3.parnet = c
        g.rchild = c
        c.parent = g

        s2 = g.lchild
        p.rchild =s2
        if s2:
            s2.parent = p
        g.lchild = p
        p.parent = g

        # 更新bf
        if g.bf > 0:
            p.bf = -1
            c.bf = 0
        elif g.bf < 0:
            p.bf = 0
            c.bf = 1
        else:  # 插入的是g
            p.bf = 0
            c.bf = 0
        return g

    def rotate_left_right(self, p, c):
        g = c.rchild

        s2 = g.lchild
        c.rchild = s2
        if s2:
            s2.parent = c
        g.rchild = c
        c.parent = g

        s3 = g.rchild
        p.lchild = s3
        if s3:
            s3.parent = p
        g.rchild = p
        p.parent = g

        #更新bf
        if g.bf < 0:
            p.bf = 1
            c.bf = 0
        elif g.bf > 0:
            p.bf = 0
            c.bf = -1
        else:
            p.bf =0
            c.bf =0
        return g

    def insert_no_rec(self, val):  # 覆盖掉二叉搜索树的插入函数
        # 1.和BST一样，插入
        p = self.root
        if not p:  # 空树
            self.root = AVLNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:  # 左孩子不存在
                    p.lchild = AVLNode(val)
                    p.lchild.parent = p
                    node = p.lchild  # node存储插入的节点
                    break
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = AVLNode(val)
                    p.rchild.parent = p
                    node = p.rchild
                    break
            else:  # val =p p.data
                return

        # 2.更新balance factor
        while node.parent:
            if node.parent.lchild == node:  # 传递是从左子树来的 左子树更沉
                #更新node.parent的bf -= 1
                if node.parent.bf < 0:  # 原来node.parent.bf == -1, 更新之后变成-2 旋转
                    # 做旋转
                    # 看node哪边沉
                    g = node.parent.parent  # 为了连接旋转之后的子树
                    x = node.parent  # 旋转前此树的根节点
                    if node.bf > 0:
                        n = self.rotate_left_right(node.parent, node)
                    else:  # 左边沉
                        n =self.rotate_right(node.parent, node)
                    # 记得把n和g连起来
                elif node.parent.bf > 0:  # 原来node.parent.bf = 1, 更新之后变成0 不需要旋转
                    node.parent.bf = 0
                    break
                else:  # 原来的node.parent.bf = 0, 更新之后变成-1 不需要旋转
                    node.parent.bf = -1
                    node = node.parent 
                    continue  # 继续往上看是否需要旋转
            else:  # 传递是从右子树来的 右子树更沉了
                if node.parent.bf > 0:  # 原来node.parent.bf ==1 , 更新后变成2
                    # 做旋转
                    # 看node哪边沉
                    g = node.parent.parent  # 为了连接旋转之后的子树
                    x = node.parent  # 旋转前此树的根节点
                    if node.bf < 0:
                        n = self.rotate_right_left(node.parent, node)
                    else:  # node.bf = -1
                        n = self.rotate_left(node.parent, node)
                    # 记得连起来
                elif node.parent.bf < 0:  # 原来node.parent.bf ==-1 , 更新后变成0
                    node.parent.bf = 0
                    break
                else:  # 原来的node.parent.bf = 0, 更新之后变成1
                    node.parent.bf = 1
                    node = node.parent
                    continue

            #  连接旋转后的子树
            n.parent = g
            if g:  # g不是空
                if x == g.lchild:
                    g.lchild = n
                else:
                    g.rchild = n
                break
            else:  # g是空
                self.root = n
                break

tree = AVLTree([9,8,7,6,5,4,3,2,1])

tree.pre_order(tree.root)
print("")
tree.in_order(tree.root)























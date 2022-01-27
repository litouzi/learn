
class BiTreeNode:  # 二叉树节点
    def __init__(self, data):
        self.data = data  
        self.lchild = None  # 左孩子
        self.rchild = None  # 右孩子
        self.parent = None  # 祖先

class BST:  # 二叉搜索树
    #构造
    def __init__(self, li=None):  # 传入列表的值构成树
        self.root = None
        if li:
            for val in li:
                self.insert_no_rec(val)  # 用非递归插入函数 插入整个列表的值 构造整棵二叉搜索树

    # 查询
    def query(self, node, val):  # 递归查询 传入节点递归用
        if not node:  # 节点为空
            return None
        # 节点不为空
        if node.data < val:  # 值大 在右边 递归右孩子
            return self.query(node.rchild, val)
        elif node.data > val:  # 值小 在左边 递归左孩子
            return self.query(node.lchild, val)
        else:  # 值相等 查找到 返回此节点
            return node
    def query_no_rec(self, val):  # 非递归查询
        p = self.root  # 从根开始查找
        while p:  # 如果根值不为空
            if p.data < val:  # 值小 在左边 左孩子循环
                p = p.rchild
            elif p.data > val:
                p = p.lchild
            else:  
                return p
        return None  # 根值为空

    # 插入
    def insert(self, node, val):  # 递归插入 # 传入节点和要插入的值
        if not node:  # 如果node是空(树为空或者是空孩子) 直接把值插上去 节点递归用
            node = BiTreeNode(val)
        elif val < node.data:  # 如果要插入的值小于传入的节点的值 
            node.lchild = self.insert(node.lchild, val)  # 那么寻找这个结点的左边进行插入 递归左孩子 左边node.lchild仅仅承接(指向)返回值 可以不指向 会回收销毁这个返回值 也可以去掉return不返回了
            node.lchild.parent = node  # 规定祖先 尤其对于最后那个插入的新创建的节点
        elif val > node.data:  # 如果要插入的值大于要传入节点的值
            node.lchild = self.insert(node.rchild, val)  # 那么寻找这个结点的右边进行插入 递归右孩子 左边node.rchild仅仅承接(指向)返回值
            node.rchild.parent = node  # 规定祖先 尤其对于最后那个插入的新创建的节点
        # 如果要插入的值等于节点的值 可以规定不能有相同的或者规定都往右插入
        return node  

    def insert_no_rec(self, val):  # 非递归插入 传入要插入的值 节点默认为根 构造起整棵树
        p = self.root
        if not p:  # 空树
            self.root = BiTreeNode(val)  # 直接插入
            return  # 插入后跳出
        while True:  # 不是空树
            if val < p.data:
                if p.lchild:  # 左孩子不为空
                    p = p.lchild  # 循环左孩子
                else:  # 左孩子为空
                    p.lchild = BiTreeNode(val)  # 直接插入左孩子
                    p.lchild.parent = p  # 规定这个新插入的节点的祖先
                    return  # 插入之后跳出 相当于break
            elif val > p.data:
                if p.rchild:  
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
            else:  # 值相等不插入
                return

    # 删除
    def __remove_node_1(self, node):  # 情况1：node是叶子节点 直接删掉
        if not node.parent:  # 是根节点也是叶子节点 只有一个节点 直接删除
            self.root = None
        if node == node.parent.lchild:  # node是它父亲的左孩子
            node.parent.lchild = None  # 删掉此节点 同时也说明父亲没有此孩子了
            #node.parent = None
        else:  # node是它父亲的右孩子
            node.parent.rchild = None
        
    def __remove_node_21(self, node):  # 情况21：node只有一个左孩子
        if not node.parent:  # 根节点 没有祖先
            self.root = node.lchild  # 把根换给左孩子
            node.lchild.parent = None  # 删掉此节点 同时也说明孩子没有祖先了
        elif node == node.parent.lchild:  # 它是它祖先的左孩子
            node.parent.lchild = node.lchild  # 把祖先的左孩子和自己的左孩子连接
            node.lchild.parent = node.parent  # 它的左孩子的祖先是它的祖先
        else:  # 它是它祖先的右孩子
            node.parent.rchild = node.lchild  # 把祖先的右孩子和自己的左孩子连接
            node.lchild.parent = node.parent  # 它的左孩子的祖先是他的祖先

    def __remove_node_22(self, node):  # 情况21：node只有一个右孩子
        if not node.parent:  # 根节点 没有祖先
            self.root = node.rchild  # 把根换给左右孩子
            node.rchild.parent = None  # 删掉此节点 同时也说明孩子没有祖先了
        elif node == node.parent.lchild:  # 它是它祖先的左孩子
            node.parent.lchild = node.rchild  # 把祖先的左孩子和自己的右孩子连接
            node.rchild.parent = node.parent  # 它的右孩子的祖先是它的祖先
        else:  # 它是它祖先的右孩子
            node.parent.rchild = node.rchild  # 把祖先的右孩子和自己的右孩子连接
            node.rchild.parent = node.parent  # 它的右孩子的祖先是他的祖先


    def delete(self,val):  # 先找到值所在的节点再把它删掉
        if self.root:  # 不是空树
            node = self.query_no_rec(val)  # 先找到这个节点
            if not node:  # 如果这个节点不存在
                return False
            if not node.lchild and not node.rchild:  # 没有左孩子和右孩子 情况1叶节点
                self.__remove_node_1(node)  # 用第一种删除方法删除此节点
            elif not node.rchild:  # 只有一个左孩子 情况2.1
                self.__remove_node_21(node)
            elif not node.rchild:  # 只有一个右孩子 情况2.2
                self.__remove_node_22(node)
            else:  # 两个孩子都有 情况3
                min_node = node.rchild  # 去右子树找右子树的最小节点
                while min_node.lchild:  # 有左孩子不为空 就往左孩子游历
                    min_node = min_node.lchild
                # 此时min_node已经指向右子树的最小节点
                node.data = min_node.data  # 将这个节点的数据换成右子树最小数据
                # 删除min_node 至多有一个右孩子 可能是没有右孩子 情况1 或者有一个右孩子 情况2.2
                if min_node.rchild:  # 有一个右孩子 情况2.2
                    self.__remove_node_22(min_node)
                else:  # 没有孩子 情况1
                    self.__remove_node_1(min_node)

    # 遍历
    def pre_order(self,root):  # 前序遍历 递归 先自己再左子树再右子树
        if root:  # 不是空
            print(root.data,end=',')
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    def in_order(self,root):  # 中序遍历 先左子树再自己再右子树
        if root:
            self.in_order(root.lchild)
            print(root.data,end=',')
            self.in_order(root.rchild)

    def post_order(self,root): # 后序遍历 先左再右后自己
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data,end=',')



# tree = BST([4,6,7,9,21,3,5,8])
# tree.pre_order(tree.root)
# print("")
# tree.in_order(tree.root)  # 中序遍历已经排好序3,4,5,6,7,8,9,21, 先左再自己再右 先小再中再大
# print("")
# tree.post_order(tree.root)
# print("")
# tree.insert_no_rec(10)  # 插入10
# tree.in_order(tree.root)  # 中序遍历
# print("")
# print(tree.query_no_rec(10).data)  # 查询节点 打印它的值
# tree.delete(10)  # 删除数据为10的这个节点
# tree.in_order(tree.root)
# print("")




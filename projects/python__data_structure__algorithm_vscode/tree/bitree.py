

class BiTreeNode:
    def __init__(self, data):
        self.data = data  
        self.lchild = None  # 左孩子
        self.rchild = None  # 右孩子

# 创建树的节点
a = BiTreeNode("A")
b = BiTreeNode("B")
c = BiTreeNode("C")
d = BiTreeNode("D")
e = BiTreeNode("E")
f = BiTreeNode("F")
g = BiTreeNode("G")

# 连接各节点组成树
e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f

root = e

#print(root.lchild.rchild.data)  # C

def pre_order(root):  # 前序遍历 递归 先自己再左子树再右子树
    if root:  # 不是空
        print(root.data,end=',')
        pre_order(root.lchild)
        pre_order(root.rchild)

def in_order(root):  # 中序遍历 先左子树再自己再右子树
    if root:
        in_order(root.lchild)
        print(root.data,end=',')
        in_order(root.rchild)

def post_order(root): # 后序遍历 先左再右后自己
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data,end=',')

from collections import deque
# 层次遍历 先自己再左右孩子 再左右孩子的孩子 不止适用于二叉树
def lever_order(root):  # 用队列实现 一层层 弄这一层的时候产生下一层入队尾
    queue = deque()
    queue.append(root)  # 让根进队
    while len(queue) > 0:  # 只要队不空 出队一个元素然后进队它的孩子们
        node = queue.popleft()  # 出队一个元素并打印
        print(node.data, end=',')
        if node.lchild:  # 有左孩子的话让左孩子入队尾(下一层)
            queue.append(node.lchild)
        if node.rchild:  # 有右孩子的话让右孩子入队尾(下一层)
            queue.append(node.rchild)


#pre_order(root)
#in_order(root)
#post_order(root)
lever_order(root)




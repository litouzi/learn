class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

# a = Node(1)
# b = Node(2)
# c = Node(3)
# a.next = b
# b.next = c

# print(a.next.next.item)

# li = [1,2,3,4,5]
# li[2]

def create_linklist_head(li):  # 头插法
    head = Node(li[0])  # 根据第一个结点创建头结点
    for element in li[1:]:
        node = Node(element)  # 在循环中创建一个新的结点
        node.next = head  # 使新结点指向在它之前创建的结点
        head = node  # 使新的结点成为新的头 (完成一个新头的插入)
    return head

def create_linklist_tail(li):  # 尾插法
    head = Node(li[0])  # 根据第一个结点创建头结点
    tail = head  # 第一个头结点也是尾结点
    for element in li[1:]:
        node = Node(element)  # 在循环中创建一个新的结点
        tail.next = node  # 使得尾(前一个元素)指向新的结点(下一个元素)
        tail = node  # 使新的结点成为新的尾 (完成一个尾的插入)
    return head  # 由于结点自身只有next 只能从头找元素




def print_linklist(lk):  # lk为头 只要lk不为None 循环打印 遍历链表
    while lk:
        print(lk.item, end=',')
        lk = lk.next

lk1 = create_linklist_head([1,2,3])
lk2 = create_linklist_tail([1,2,3,6,8])
print_linklist(lk1)  # 3,2,1
print_linklist(lk2)  # 1,2,3,6,8
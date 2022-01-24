from collections import deque
from os import curdir  # 使用现成队列

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

dirs = [  # 用一个列表封装四个方向
    lambda x,y: (x+1,y),  # 下
    lambda x,y: (x-1,y),  # 上
    lambda x,y: (x,y+1),  # 右
    lambda x,y: (x,y-1),  # 左
]

def print_r(path):  # 通过全部路径path输出真正路径realpath
    curNode = path[-1]  # 将结点放在最后的那个值 [-1]取最后的元素

    realpath = []  # 用一个列表存储真正通路的路径

    while curNode[2] != -1:  # 没有游历完所有祖先 没有回到起点 从最后一个元素开始找真正路径
        realpath.append((curNode[0], curNode[1]))  # realpath.append((curNode[0:2]) 将结点加入真正路径
        curNode = path[curNode[2]]  # 上一个点由这一个点的位置找出  

    realpath.append(curNode[0:2])  # 把循环完之后的当前结点(起点)加入真正路径列表
    realpath.reverse()  # 倒序
    for node in realpath:  # 循环输出路径
        print(node)

def maze_path_queue(x1,y1,x2,y2):
    queue = deque()  # 创建一个队列用来存当前考虑的结点
    queue.append((x1, y1, -1))  # 添加起点 三元元组 存了结点坐标和前一个结点的列表位置
    path = []  # 额外的列表
    while len(queue) > 0:  # 只要列表不为空 就有路可寻

        curNode = queue.popleft()  # 把队列元素出队到当前结点 起点不考虑了 变为走过的路径 考虑下一步的结点
        path.append(curNode)  #将当前判断(走上去的点加入额外的列表 记录路径) 
        if curNode[0] == x2 and curNode[1] == y2:  # 找到终点 输出所有路径
            print_r(path)
            return True

        for dir in dirs:  # 在当前结点的上下左右寻路
            nextNode = dir(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:  # 通路
                queue.append((nextNode[0],nextNode[1], len(path)-1))  # 则把新的结点加入队列 变为当前要考虑的结点 位置为path的长度-1
                #此处不break 因为不是找到一个可行结点就往里走(深度) 而是找出此处的所有可行结点放入队列(广度)
                #找完所有当前要考虑的结点之后 依次弹出当前要考虑的结点到当前结点curNode再往下进行寻路
                maze[nextNode[0]][nextNode[1]] = 2  # 将新的结点(将要用line29 curNode = queue.pop()走上去的结点)(树叶)置2
    else:  # while跳出 无路可寻
        print("没有路")
        return False

maze_path_queue(1,1,8,8)





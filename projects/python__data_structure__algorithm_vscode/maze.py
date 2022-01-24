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

def maze_path(x1,y1,x2,y2):  # (x1,y1)起点位置(元组) (x2,y2)终点位置 x行标 y列标
    stack = []
    stack.append((x1, y1))
    while(len(stack)>0):  # 栈不为空 有路时寻路

        curNode = stack[-1]  # 当前结点
        if curNode[0] == x2 and curNode[1] == y2:  #走到终点了
            for p in stack:  # 输出路径 游历一遍栈
                print(p)
            return True  # 寻路成功

        #(x,y)四个方向 上(x-1,y) 下(x+1,y) 左(x,y-1) 右(x,y+1)
        for dir in dirs:  # 找四个方向能不能走
            nextNode = dir(curNode[0],curNode[1])  # 将当前点curNode的坐标传进dirs进行四向循环
            
            # 如果下一个结点能走
            if maze[nextNode[0]][nextNode[1]] == 0:  # 通路
                stack.append(nextNode)  # 把将要走过的路加到栈里面 走过去了 此时curNode = stack[-1]  # 当前结点 和nextNode相等
                maze[nextNode[0]][nextNode[1]] = 2  # 用2标记走过的路
                break  # 能找到一个就break 走过去

        else:  # 对于for 找不到通路 都是死路(墙或已走过的路)
            maze[nextNode[0]][nextNode[1]] = 2  # 无路走时也将此结点置2 (至少对于起点 将起点置2弹出去 变为空栈)
            stack.pop()  # 出栈 退回去

    else:  # while跳出 栈为空 没路
        print("没有路")
        return False

maze_path(1,1,8,8)  # 起点(1,1)终点(8,8)迷宫问题

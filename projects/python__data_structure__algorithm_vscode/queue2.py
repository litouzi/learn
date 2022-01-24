from collections import deque  # de双向queue队列

q = deque([1,2,3], 5)  # 创建含初始值的队列 长度为5(队满会自动出队) (left头end尾)
q.append(4)  # 队尾进队
print(q.popleft())  # 队首出队

# # 用于双向队列
# q.appendleft(1)  # 队首进队
# q.pop()  # 队尾出队
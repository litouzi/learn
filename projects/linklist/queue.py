class Queue:
    def __init__(self,size = 100):  # 创建列表时需要先确定最大值Maxsize
        self.queue = [0 for _ in range(size)]
        self.size = size
        self.rear = 0  # 队尾指针
        self.front = 0  # 队首指针

    def push(self, element):  # 进队 可能导致队满
        if not self.is_filled():  # 队不满 可以进队
            self.rear = (self.rear + 1) % self.size # 将尾向前移动1
            self.queue[self.rear] = element  # 使进入的新值处于尾新指向的位置
        else:  # 队满 无法进队
            raise IndexError("Queue is filled.")

    def pop(self):  # 出队 可能导致队空
        if not self.is_empty():  # 队不空 可以出队
            self.front = (self.front + 1) % self.size  # 将头向前移动1指向要出去的值(原本front指向空)
            return self.queue[self.front]  # 取得此处的值
        else:  # 队空 无法出队
            raise IndexError("Queue is empty.")
    
    def is_empty(self):  # 队空
        return self.rear == self.front #头尾指针指向相同时返回队空true

    def is_filled(self):  # 队满
        return (self.rear + 1) % self.size == self.front

q = Queue(5)  # 创建一个长度5(实际占空间6 能存5个值)的(环形)队列
for i in range(4):
    q.push(i)
print(q.pop())
q.push(4)






import turtle


class Stack:
    def __init__(self):
        self.stack = []

    def push(self,element):  # 压栈
        self.stack.append(element)

    def pop(self):  # 弹栈
        return self.stack.pop()

    def get_top(self):  # 取栈顶
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None
    def is_empty(self):  # 栈为空
        return len(self.stack) == 0


# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.pop())

def brace_match(s):  # 括号匹配
    match = {')':'(',']':'[','}':'{'}  # 字典
    stack = Stack()
    for ch in s:
        if ch in{'(','[','{'}:  # 让所有左括号进栈
            stack.push(ch)
        else:  #ch in {'}',']',')'} 是右括号
            if stack.is_empty():  # 栈为空 没有与这个右括号相匹配的左括号 报错
                return False
            elif stack.get_top() == match[ch]:  # 栈不为空 栈顶的左括号与这个右括号匹配 弹出匹配的左括号
                stack.pop()
            else: #stack.get_top() != match[ch]  # 栈不为空 但是栈顶的括号不匹配 报错
                return False
    if stack.is_empty(): # 最后进栈的左括号都匹配到右括号弹出 栈为空
        return True
    else:
        return False

print(brace_match('[{()}(){()}[]({}){}]'))
print(brace_match('[{]}'))


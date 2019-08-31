"""
数据结构
"""


# 二维数组中，每行从左到右递增，每列从上到下递增，给出一个数，判断它是否在数组中
def find_integer(matrix, num):
    """
    [
        [5,6,7,8],
        [6,7,8,9],
    ]
    """
    if not matrix:
        return False
    rows, cols = len(matrix), len(matrix[0])
    row, col = rows - 1, 0
    while row >= 0 and col <= cols - 1:
        if matrix[row][col] == num:
            return True
        elif matrix[row][col] > num:
            row -= 1
        else:
            col += 1
    return False


# 把字符串中的空格替换成'20%'
def change_space(s):
    return s.replace(' ', '20%')


# 从尾到头打印单链表
def print_links(links):
    stack = []
    while links:
        stack.append(links.val)
        links = links.next
    while stack:
        print(stack.pop())


# 用两个栈实现队列
# 用两个栈实现队列，分别实现入队和出队操作 思路：一个栈负责入队，另一个负责出队，出栈为空则从入栈中导入到出栈中
class MyQueue(object):
    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        while self.stack:
            self.stack2.append(self.stack.pop())
        return self.stack2.pop() if self.stack2 else u'队列为空'


# 要求：把递增数组的前面部分数字移到队尾，求数组中的最小值，例如[3,4,5,6,1,2]


# 斐波那契数列
def fib(num):
    a, b =0, 1
    for i in range(num):
        yield b
        a, b = b, a + b
    return a, b


# 链表实现
class Node():
    def __init__(self, element=None):
        self.e = element
        self.next = None


head = Node()
n1 = Node(111)
n2 = Node(222)
n3 = Node(333)
head.next = n1
n1.next = n2
n2.next = n3


def append(node, element):
    """
    我们往 node 的末尾插入一个元素
    :param node: 是一个node 实例
    :param element:
    :return:
    """
    n = node
    while n.next is not None:
        n = n.next
    new_node = Node(element)
    n.next = new_node


def prepend(head, element):
    n = Node(element)
    n.next = head.next
    head.next = n


def pop(head):
    """
    删除最末尾的元素
    :param head:
    :return:
    """
    n1 = head
    n = head
    while n.next is not None:
        n = n.next

    while n1.next != n:
        n1 = n1.next
    n1.next = None
    return n.e



class HashTable(object):
    def __init__(self):
        self.table_size = 10007
        self.table = [0] * self.table_size

    def has_key(self, key):
        pass

    def __contains__(self, item):
        return self.has_key(item)

    def has_key(self, key):
        index = self._index(key)
        v = self.table[index]
        if isinstance(v, list):
            for kv in v:
                if kv[0] == key:
                    return True
        return False

    def _insert_at_index(self, index, key, value):
        # 检查下标处是否第一次插入数据
        v = self.table[index]
        data = [key, value]
        if isinstance(v, int):
            self.table[index] = [data]
        else:
            self.table[index].append(data)

    def add(self, key, value):
        index = self._index(key)
        self._insert_at_index(index, key, value)

    def get(self, key, default_value=None):
        index = self._index(key)
        v = self.table[index]
        if isinstance(v, list):
            for kv in v:
                if kv[0] == key:
                    return kv[1]
        return default_value



    def _index(self, key):
        return self._hash(key) % self.table_size

    def _hash(self, s):
        n = 1
        f = 1
        for i in s:
            n += ord(i)*f
            f *= 10
        return n




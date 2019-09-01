class A:
    name = "A"

    def __init__(self):
        self.name = 'obj'


a = A()
print(a.name)


# MRO算法 深度优先算法、广度优先算法
# 现在用C3算法
#

class D:
    pass

class C(D):
    pass

class B(D):
    pass

class A(B,C):
    pass


print(A.__mro__)
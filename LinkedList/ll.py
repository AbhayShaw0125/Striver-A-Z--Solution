class _Node:
    __slots__='_element','_next'
    def __init__(self,element,next):
        self._element=element
        self._next=next


n1=_Node(8,None)
n2=_Node(11,None)
n1._next=n2
print(n1._next)
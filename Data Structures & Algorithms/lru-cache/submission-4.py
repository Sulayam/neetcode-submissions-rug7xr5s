class Node:
    def __init__(self, key: int, value: int):
        self.key=key
        self.value=value
        self.prev=self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cachemap={}
        self.left,self.right=Node(0,0),Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left
    
    def remove(self, node:Node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cachemap:
            self.remove(self.cachemap[key])
            self.insert(self.cachemap[key])
            return self.cachemap[key].value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cachemap:
            self.remove(self.cachemap[key])

        self.cachemap[key]=Node(key,value)
        self.insert(self.cachemap[key])

        if len(self.cachemap) > self.cap:
            lru=self.left.next
            self.remove(lru)
            del self.cachemap[lru.key]

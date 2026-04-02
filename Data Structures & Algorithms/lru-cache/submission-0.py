class Node:
    def __init__(self, key,val, prev= None, next = None):
        self.key = key
        self.val= val 
        self.prev = prev
        self.next = next 



class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        self.cache = {}
        

    def get(self, key: int) -> int:
        if key in self.cache:
            
            #deletion
            self.cache[key].prev.next = self.cache[key].next
            self.cache[key].next.prev = self.cache[key].prev

            #insertion
            self.right.prev.next =self.cache[key]
            self.cache[key].prev = self.right.prev
            self.cache[key].next = self.right
            self.right.prev = self.cache[key]

            return self.cache[key].val
        return -1 
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            #deletion
            self.cache[key].prev.next = self.cache[key].next
            self.cache[key].next.prev = self.cache[key].prev

            #insertion
            self.right.prev.next =self.cache[key]
            self.cache[key].prev = self.right.prev
            self.cache[key].next = self.right
            self.right.prev = self.cache[key]

            self.cache[key].val = value
        else:
            self.cache[key] = Node(key, value)
            self.right.prev.next =self.cache[key]
            self.cache[key].prev = self.right.prev
            self.cache[key].next = self.right
            self.right.prev = self.cache[key]   

            if len(self.cache) > self.cap:
                key =self.left.next.key
                self.left.next = self.left.next.next 
                self.left.next.prev = self.left
                del self.cache[key]   
            

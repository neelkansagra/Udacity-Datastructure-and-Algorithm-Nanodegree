class DoubleNode:
    def __init__(self, key,value):
        self.value = value
        self.key = key
        self.next = None
        self.previous = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail
    
    def add_last(self, key, value):
        if self.tail is None:
            self.tail = DoubleNode(key,value)
            self.head = self.tail
            return
        self.tail.next = DoubleNode(key,value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next

    def add_first(self,key, value):
        if self.head is None:
            self.head = DoubleNode(key,value)
            self.tail = self.head
            return
        self.head.previous = DoubleNode(key,value)
        self.head.previous.next = self.head
        self.head = self.head.previous

    def remove_using_node(self,node):                  #Removes node using reference to the node
        if node.previous and node.next:
            node.previous.next = node.next
            node.next.previous = node.previous
            node.next = None
            node.previous = None
        elif node.previous:
             self.tail = node.previous
             node.previous.next = None
             node.previous = None
        elif node.next:
             self.head = node.next
             node.next.previous = None
             node.next = None
        else:
            if self.head:
                self.head = None
                self.tail = None
        
    def print_list(self):             #helper to print Doubly LinkedList
        current = self.head
        while current:
            print(current.key,current.value)
            current = current.next
    
class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.num_items = 0
        self.lookup_table = dict()                              #Lookup table for storing references to nodes
        self.doubly_list = DoublyLinkedList()
        pass

    def get(self, key):
        if key in self.lookup_table:
            
           #removing the node from it's original position
           node_to_be_removed = self.lookup_table[key]
           self.doubly_list.remove_using_node(node_to_be_removed)
           
           #adding it to the front of doublyLinked List
           self.doubly_list.add_first(key,self.lookup_table[key].value)
           self.lookup_table[key] = self.doubly_list.get_head()
           
           return self.lookup_table[key].value
        
        else:
           return -1
        pass
    def print_doublylist(self):
        self.doubly_list.print_list()

    def set(self, key, value):
        
        if self.capacity == 0:
            print("Can't perform operations on 0 capacity cache")
            return
        
        if key in self.lookup_table:                           #Updating the value of duplicate key by removing the present key
             node_to_be_removed = self.lookup_table[key]
             self.doubly_list.remove_using_node(node_to_be_removed)
         
             #updating the value 
             self.doubly_list.add_first(key,value)
             self.lookup_table[key] = self.doubly_list.get_head()
             
        elif self.num_items < self.capacity:
            
            self.doubly_list.add_first(key,value)
            self.lookup_table[key] = self.doubly_list.get_head()
            self.num_items+=1
            
        else:
            
            #removing LRU node
            node_to_be_removed = self.doubly_list.get_tail()
            remove_key = node_to_be_removed.key
            
            self.doubly_list.remove_using_node(node_to_be_removed)
            del self.lookup_table[remove_key]

            #adding the given node
            self.doubly_list.add_first(key,value)
            self.lookup_table[key] = self.doubly_list.get_head()
        

# Normal Case:
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))
# returns 1
print(our_cache.get(2))
# returns 2
print(our_cache.get(9))
# returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Edge Case:
our_cache = LRU_Cache(2)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(1, 10)
print(our_cache.get(1))
# should return 10
print(our_cache.get(2))
# should return 2

our_cache = LRU_Cache(0)
our_cache.set(1, 1)
# should print some message like "Can't perform operations on 0 capacity cache"
print(our_cache.get(1))
# should return -1

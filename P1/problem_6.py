class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        
    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size

def union(llist_1, llist_2):
     
    union = LinkedList()                        # creating a new instance of union
    
    if llist_1 is None:
        current = None
        
    else:
       current = llist_1.head
       
    set_of_node = set()                       
    while current:
        
        if current.value in set_of_node:        # if the current value is present in set then skip
            current = current.next
            continue
        
        set_of_node.add(current.value)          # add the value to set and to the union list
        union.append(current.value)        
        current = current.next
        
    if llist_2 is None:                         # same procedure for list2 
        current = None           
        
    else:
        current = llist_2.head
        
    while current:
        if current.value in set_of_node:     
            current = current.next
            continue
        
        set_of_node.add(current.value)
        union.append(current.value)
        current = current.next
        
    return union

def intersection(llist_1, llist_2):
    
    intersect = LinkedList()
    current = union(llist_1,None).head              # this step removes duplicate values in the given list
    
    set_of_node = set()
    
    while current:
        
        if current.value in set_of_node:            # if current node is in set then add it to the intersect list
            current = current.next
            continue
        
        set_of_node.add(current.value)
        current = current.next

    current = union(None,llist_2).head              # Same procedure for list2
    
    while current:
        
        if current.value in set_of_node:
            intersect.append(current.value)
            current = current.next
            continue
        
        set_of_node.add(current.value)
        current = current.next
        
    return intersect
  


# **** Test case 1 ****
# Normal Inputs

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 -> 
print (intersection(linked_list_1,linked_list_2))
# 6 -> 4 -> 21 -> 


# **** Test case 2 ****
# No Intersection

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 
print (intersection(linked_list_3,linked_list_4))
# (No Output)


# **** Test case 3 ****
# Element 1 empty

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
# 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
print (intersection(linked_list_3,linked_list_4))
# (No Output)


# **** Test case 4 ****
# Element 2 empty

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 
print (intersection(linked_list_3,linked_list_4))
# (No Output)


# **** Test case 5 ****
# Element 1 None

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = None
element_2 = [1,7,8,9,11,21,1]

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
# 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 
print (intersection(linked_list_3,linked_list_4))
# (No Output)


# **** Test case 6 ****
# Element 2 None

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = None

for i in element_1:
    linked_list_3.append(i)

print (union(linked_list_3,linked_list_4))
# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 ->
print (intersection(linked_list_3,linked_list_4))
# (No Output)


# **** Test case 7 ****
# Identical list

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [1,2,3,4]
element_2 = [1,2,3,4]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
# 1 -> 2 -> 3 -> 4 ->
print (intersection(linked_list_3,linked_list_4))
# 1 -> 2 -> 3 -> 4 -> 


# **** Test case 8 ****
# Same Reference

linked_list_3 = LinkedList()

element_1 = [1,2,3,4]

for i in element_1:
    linked_list_3.append(i)

print (union(linked_list_3,linked_list_3))
# 1 -> 2 -> 3 -> 4 ->
print (intersection(linked_list_3,linked_list_3))
# 1 -> 2 -> 3 -> 4 -> 

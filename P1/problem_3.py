import sys
import heapq

class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.left_child = None
        self.right_child = None
        
    def get_key(self):
        return self.key
    
    def get_value(self):
        return self.value
    
    def set_value(self,value):
        self.value = value
    
    def set_left_child(self,child):
        self.left_child = child
    
    def set_right_child(self,child):
        self.right_child = child
        
    def get_left_child(self):
        return self.left_child
    
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def get_right_child(self):
        return self.right_child
    
    def __gt__(self, other):
        
        return self.value > other.value


class Tree(Node):
    def __init__(self):
        self.root = None
    def set_root(self,key,value):
        self.root = Node(key,value)
    def get_root(self):
        return self.root
        
def freq_of_char(data):                     # calculates the frequency of characters in a string and return a dictionary
    
    freq = dict()
    for char in data:
        
        if char not in freq:
            freq[char] = 1
            
        else:
            freq[char]+=1
            
    return freq

def assign_codes(node,bin_code,dict_of_codes):                  # traversers the tree and assigns binary codes to each leaf node in form of a dictionary
    
    if len(node.get_key()) == 1:                                # if the node is leaf then assign that code to corresponding char in dictionary
        if bin_code=='':
            bin_code = '0'
            
        dict_of_codes[node.get_key()] = bin_code
        return
    
    assign_codes(node.get_left_child(),bin_code+'0',dict_of_codes)
    assign_codes(node.get_right_child(),bin_code+'1',dict_of_codes)

def huffman_encoding(data):
    freq = freq_of_char(data)
    
    heap = []
    for i in freq:
        heapq.heappush(heap,Node(i,freq[i]))

    tree = Tree()
    if len(heap)==1:                                           #edge case of string having only 1 unique character
        node = heapq.heappop(heap)
        tree.set_root(node.get_key(),node.get_value())         
   
    while len(heap) > 1:
        node1= heapq.heappop(heap)                              # pop 2 nodes from the priority queue
        node2= heapq.heappop(heap)
        
        tree.set_root(node1.get_key()+node2.get_key(),node1.get_value()+node2.get_value())   # merge both the nodes by adding its frequency and appending characters
        tree.get_root().set_left_child(node1)
        tree.get_root().set_right_child(node2)
        
        heapq.heappush(heap,tree.get_root())                 # push the merged node inside priority queue

    bin_codes =dict()
    assign_codes(tree.get_root(),'',bin_codes)                 # assigns each unique character in the given string a unique binary code 
    
    encoded_string =''
    for char in data:
        encoded_string+=bin_codes[char]

    return encoded_string, tree.get_root()

def huffman_decoding(data,root_node):
    decoded_string = ''
    current = root_node

    
    for char in data:
        if char == '0':                              #if char is 0 we move left

            if current.get_left_child():
               current = current.get_left_child()
               
            if len(current.get_key()) == 1:          #if we reach the leaf node then append its char to decoded string and set current to root_node
                
                decoded_string += current.get_key()
                current = root_node
                
        else:
            
            if current.get_right_child():
               current = current.get_right_child()      #if char is 1 we move right
            
            if len(current.get_key()) == 1:          #if we reach the leaf node then append its char to decoded string and set current to root_node 
                decoded_string +=current.get_key()
                current = root_node
                
    return decoded_string

if __name__ == "__main__":
    codes = {}
    print("**** Test 1 ****\nRegular Sentence\n")
    test_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(test_sentence)))
    print ("The content of the data is: {}\n".format(test_sentence))

    encoded_data, tree = huffman_encoding(test_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the decoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


    print("**** Test 2 ****\nSingle Character\n")
    test_sentence = "a"

    print ("The size of the data is: {}\n".format(sys.getsizeof(test_sentence)))
    print ("The content of the data is: {}\n".format(test_sentence))

    encoded_data, tree = huffman_encoding(test_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))


    print("**** Test 3 ****\nSingle Character Repeated\n")
    test_sentence = "aaaaaaa"

    print ("The size of the data is: {}\n".format(sys.getsizeof(test_sentence)))
    print ("The content of the data is: {}\n".format(test_sentence))

    encoded_data, tree = huffman_encoding(test_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))


    print("**** Test 4 ****\nSame Letter, Different Case\n")
    test_sentence = "aaAAbbBB"

    print ("The size of the data is: {}\n".format(sys.getsizeof(test_sentence)))
    print ("The content of the data is: {}\n".format(test_sentence))

    encoded_data, tree = huffman_encoding(test_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))


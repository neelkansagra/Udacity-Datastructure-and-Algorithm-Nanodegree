import time
import hashlib


class Block:

    def __init__(self, timestamp,data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

    def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = "We are going to encode this string of data!".encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()

class BlockChain:
    def __init__(self):
        self.tail = None
        self.size = 0
        
    def add_block(self,data,):
        if self.tail is None:
            self.tail = Block(time.time(),data,None)
            
        else:
            self.tail = Block(time.time(),data,self.tail)
        self.size+=1

    def print_blockchain(self):
        current = self.tail
        if current is None:
            print("[]")
            
        else:
            while current:
                print([current.timestamp,current.data,current.hash])
                current = current.previous_hash

    def size(self):
        return self.size

blockchain = BlockChain()
blockchain.add_block("hi ")
blockchain.add_block("hello ")
blockchain.add_block("how ")
blockchain.add_block("are ")
blockchain.add_block("you ")
blockchain.print_blockchain()
        
        
        

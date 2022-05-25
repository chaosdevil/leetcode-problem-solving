class BloomFilter(object):
    
    #Initialize bitarray
    def __init__(self,k,m):
        self.bit_array_size = m
        self.bit_array = bitarray('0')*m
        self.num_of_hash_functions = k
    
    #add element to bitarray
    def add(self,item):
        collisions = 0
        i = 0
        for i in range(self.num_of_hash_functions):
            index = mmh3.hash(item, i) % self.bit_array_size
            if self.bit_array[index] == True and i <= 5:
              collisions += 1
            i += 1
            self.bit_array[index] = True
        print(collisions)
    
    #check if element exists
    def check(self,item):
        for i in range(self.num_of_hash_functions):
            index = mmh3.hash(item,i) % self.bit_array_size
            if not self.bit_array[index]:
                return False
        return True
        


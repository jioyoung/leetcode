#
# @lc app=leetcode id=460 lang=python3
#
# [460] LFU Cache
#

# @lc code=start
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key: value
        self.frequency = {} # 1: [key i, keyj] ; 2: [key k ..]
        self.freq_key = {} # key i: frequency, position
        self.minFreq = None


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            count = self.freq_key[key]
            self.frequency[count].remove(key)
            if not self.frequency[count]:
                del self.frequency[count]
                if count == self.minFreq:
                    self.minFreq += 1
            if count + 1 in self.frequency:
                self.frequency[count+1].append(key)
            else:
                self.frequency[count+1] = [key]
            self.freq_key[key] = count+1
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity <=0:
            return
        if key in self.cache:
            self.cache[key] = value
            self.get(key)
            return
        else:
            if len(self.cache) == self.capacity:

                removeKey = self.frequency[self.minFreq].pop(0)
                if not self.frequency[self.minFreq]:
                    del self.frequency[self.minFreq]
                del self.freq_key[removeKey]
                del self.cache[removeKey]
            if 1 in self.frequency:
                self.frequency[1].append(key)
            else:
                self.frequency[1] = [key]
            self.minFreq = 1
            self.cache[key] = value
            self.freq_key[key] = 1 
    
        return


        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end


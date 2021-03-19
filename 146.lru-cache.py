#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
from collections import OrderedDict
# @lc code=start
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.get(key)
            return
        
        if len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
    
        self.cache[key] = value

        return
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end


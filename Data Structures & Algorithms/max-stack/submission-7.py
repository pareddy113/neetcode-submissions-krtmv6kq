from sortedcontainers import SortedList
class MaxStack:

    # 1. stack op
    # 2. find stack's max element

    # sorted_stack = [1,4,2,3]
    # sorted_list = [1,2,3,4]


    def __init__(self):
        self.stack = SortedList()
        self.max_array = SortedList()
        
    # O(log n)
    def push(self, x: int) -> None:
        index = len(self.stack)
        self.stack.add((index, x))
        self.max_array.add((x, index))
        

    # O(log n)
    def pop(self) -> int:
        index, val = self.stack.pop()
        self.max_array.discard((val, index))
        return val
        
    # O(1)
    def top(self) -> int:
        return self.stack[-1][1]
        
    # O(1)
    def peekMax(self) -> int:
        return self.max_array[-1][0]
        

    #  O(1) + O(log n)  = O(log n)
    def popMax(self) -> int:
        value, index = self.max_array.pop()
        self.stack.discard((index, value))
        return value
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

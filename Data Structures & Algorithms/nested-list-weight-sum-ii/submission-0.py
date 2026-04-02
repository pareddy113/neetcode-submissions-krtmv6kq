# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:

        depth_map = {}

        def depth_sum_dfs(nested_list, depth, max_depth):
            
            max_sum = 0
            for item in nested_list:
                if item.isInteger():
                    max_sum += (max_depth - depth + 1) * item.getInteger()
                else:
                    max_sum += depth_sum_dfs(item.getList(), depth + 1, max_depth)
            return max_sum

        def dfs(nested_list, depth):
            
            max_depth = 0
            for item in nested_list:
                if item.isInteger():
                    depth_map[item.getInteger()] = depth
                    max_depth = max(max_depth, depth)
                else:
                    max_depth = max(max_depth, dfs(item.getList(), depth + 1))
            return max_depth
        
        max_depth = dfs(nestedList, 1)
        return depth_sum_dfs(nestedList, 1, max_depth)

        



        
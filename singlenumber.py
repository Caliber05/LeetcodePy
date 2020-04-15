class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        no_duplicate_list = []
        for i in  nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()
    
    //  Time complexity : O(n^2)O(n). We iterate through \text{nums}nums, taking O(n)O(n) time. We search the whole list to find whether there is duplicate number, 
        taking O(n)O(n) time. Because search is in the for loop, so we have to multiply both time complexities which is O(n^2)O(n).
        Space complexity : O(n)O(n). We need a list of size nn to contain elements in \text{nums}nums.//
        

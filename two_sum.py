import sys
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic_nums = {}
        dic_nums_re = {}
        for i in range(len(nums)):
            if nums[i] not in dic_nums.keys():
                dic_nums[nums[i]] = i
            else:
                dic_nums_re[nums[i]] = i
        for m in nums:
            num1 = target - m
            if num1 in dic_nums.keys():
                if num1 == m:
                    return [dic_nums[num1], dic_nums_re[m]]
                else:
                    return [dic_nums[num1], dic_nums[m]]
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        keys = {}
        for i in xrange(len(nums)):
            '''
            can't exchange the following "if",
            nums = [-1,2,8,0,0], target = 0
            '''
            print 1
            if target - nums[i] in keys:
                print 2
                return [keys[target - nums[i]], i]

            if nums[i] not in keys:
                print 3
                keys[nums[i]] = i


if __name__ == "__main__":
    #system.stdin.readline().strip()
    nums = [-1,2,8,0,1]
    target = -1
    print nums[0:2]
    so = Solution()
    res = so.twoSum(nums, target)
    print res

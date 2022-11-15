class Solution:
    def binarySearch(self, nums: list[int], target: int):
        left = 0
        right = len(nums) - 1

        while left <= right:
            # middle = (left + right) // 2
            middle = left + (right - left) //2

            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else: 
                return middle



        return -1


if __name__ == "__main__" : 
    testcase1=Solution()
    print(testcase1.binarySearch([1,2,3,4,5], 3))
    print("hello world")



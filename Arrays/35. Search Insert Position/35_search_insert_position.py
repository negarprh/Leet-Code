class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        begin_index = 0  # first index in the list
        # Last index in the list which made from then length
        end_index = (len(nums) - 1)

        while begin_index <= end_index:
            mid_index = begin_index + (end_index - begin_index) // 2
            mid_index_value = nums[mid_index]
            if target == mid_index_value:
                return mid_index
            elif target < mid_index_value:
                end_index = mid_index - 1
            else:
                begin_index = mid_index + 1
        return begin_index

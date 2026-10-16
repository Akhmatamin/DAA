class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)

        if n <= 1:
            return nums

        m = n // 2
        left_lst = nums[:m]
        right_lst = nums[m:]

        left_lst = self.sortArray(left_lst)
        right_lst = self.sortArray(right_lst)
        l, r = 0, 0

        l_len = len(left_lst)
        r_len = len(right_lst)

        sorted_lst = [0] * n
        i = 0

        while l < l_len and r < r_len:
            if left_lst[l] < right_lst[r]:
                sorted_lst[i] = left_lst[l]
                l += 1
            else:
                sorted_lst[i] = right_lst[r]
                r += 1
            i += 1

        while l < l_len:
            sorted_lst[i] = left_lst[l]
            l += 1
            i += 1

        while r < r_len:
            sorted_lst[i] = right_lst[r]
            r += 1
            i += 1

        return sorted_lst







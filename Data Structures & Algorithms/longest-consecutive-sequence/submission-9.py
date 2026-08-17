class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        a = sorted(set(nums))

        current = 1
        longest = 1

        for i in range(1, len(a)):
            if a[i] - a[i - 1] == 1:
                current += 1
            else:
                current = 1

            longest = max(longest, current)

        return longest
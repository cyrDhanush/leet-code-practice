class Solution:
    def removeZeros(self, l):
        for _ in range(l.count(0)):
            l.remove(0)
        return l
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3=sorted(self.removeZeros(nums1.copy())+self.removeZeros(nums2))
        nums1.clear()
        for i in nums3:
            nums1.append(i)
        print(nums1)
s=Solution()
s.merge([1,5,6],3,[3,5,8],3)
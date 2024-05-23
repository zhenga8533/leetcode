class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        counter = defaultdict(int)
        def countNum(nums):
            counted = set()
            for num in nums:
                if num not in counted:
                    counter[num] += 1
                    counted.add(num)
        
        countNum(nums1)
        countNum(nums2)
        countNum(nums3)
        
        return [key for key, value in counter.items() if value >= 2]

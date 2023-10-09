class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        Runtime: 171 ms  (Beats 38.66%)
        Memory: 19 MB (Beats 96.69%)
        """

        products = []
        product = 1
        zero = 0

        for num in nums:
            if num:
                product *= num
            else:
                zero += 1

        for num in nums:
            if zero:
                if num or zero > 1:
                    products.append(0)
                else:
                    products.append(product)
            else:
                products.append(product / num)
        
        return products
        

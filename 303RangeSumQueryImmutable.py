class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        cur = 0
        for n in nums:
            cur+=n
            self.prefix.append(cur)
        

    def sumRange(self, left: int, right: int) -> int:
        '''count = 0
        roll = 0
        total = 0
        for num in nums:
            if roll == 0:
                if left == count:
                    total+=num
                    roll = 1
            elif right == count:
                return total + num
            else:
                total+=num
            count+=1'''
        right_sum = self.prefix[right]
        left_sum = self.prefix[left-1] if left > 0 else 0
        return right_sum - left_sum

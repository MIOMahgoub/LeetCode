class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ## First attempt only beat 10.82% runtime at 8 ms
        '''index1 = 1
        index2 = len(numbers)
        total = numbers[index1-1] + numbers[index2-1]

        while total != target:
            if total > target:
                index2 -= 1
                total = numbers[index1-1] + numbers[index2-1]
            else:
                index1 += 1
                total = numbers[index1-1] + numbers[index2-1]
        
        return [index1, index2]'''

        ## Showed ChatGPT my code and asked how I can correct poor runtime. Said I need to stop repeating needless addition operations and minimize the repetition of this
        ## The revised code below beat 81.9% and ran in 3ms 

        # Initialize pointers
        left = 0
        right = len(numbers) - 1

        # Loop until the target is found
        while left < right:
            total = numbers[left] + numbers[right]

            # Check if the current sum matches the target
            if total == target:
                return [left + 1, right + 1]  # Convert to 1-based indexing
            elif total > target:
                right -= 1  # Move the right pointer inward
            else:
                left += 1  # Move the left pointer inward

        return []  # Should never reach here if there's a guaranteed solution
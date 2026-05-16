class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        left pointer and right pointer defined 
        left pointer points to minimum number, and right to maximum number
        Get the sum of both numbers 

        If the sum is less than the target, we must increase the left pntr
        Else decrease the right pointer

        Continue until we reach the target

        '''

        l, r = 0, len(numbers)-1

        while l < r:
            curr_sum = numbers[l] + numbers[r]

            if curr_sum < target:
                l+=1
            elif curr_sum > target:
                r-=1
            else:
                return [l+1,r+1]
        
        return False
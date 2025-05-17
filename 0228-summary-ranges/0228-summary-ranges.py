class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start = 0
        ans = []
        for end in range(len(nums)):
            if end < len(nums)-1:
                if nums[end]+1 == nums[end+1]:
                    pass
                else : 
                    ans.append([nums[start], nums[end]])
                    start = end + 1
            elif end == len(nums)-1:
                ans.append([nums[start], nums[end]])
        
        for i in range(len(ans)):
            if ans[i][0] == ans[i][1]:
                ans[i] = str(ans[i][0])
            else:
                ans[i] = str(f"{ans[i][0]}->{ans[i][1]}")
        
        return ans
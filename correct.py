class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.d = {}
        self.n = len(nums)
        def helper(i,lst) :
            if(i >= self.n) :
                # print(lst)
                ans = 0
                for j in lst :
                    ans = ans | j 
                self.d[ans] = self.d.get(ans,0) + 1
                # print(self.d)
                return  
            
            lst.append(nums[i]) 
            helper(i+1,lst) 
            lst.pop()
            helper(i+1,lst)

            return 

        helper(0,[])
        val = list(self.d.keys())
        val.sort()
        return self.d[val[-1]]

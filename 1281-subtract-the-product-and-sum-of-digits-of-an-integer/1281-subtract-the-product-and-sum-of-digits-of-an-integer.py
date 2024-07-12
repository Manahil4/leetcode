class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        assert 1<=n<=10**5
        Sum=0
        prod=1
        for i in range(len(str(n))):
            dig=n%10
            n=n//10
            Sum+=dig
            prod*=dig
        sub=prod-Sum
        return sub
        
a=Solution()  
output=a.subtractProductAndSum(234)
print(output)
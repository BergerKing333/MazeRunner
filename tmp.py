class Solution(object):
    
    
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        unused = []
        for i in range(1, n+1):
            unused.append(i)
        return helper(unused, [])
    

def helper(unused, perms):
        if len(unused) == 1:
            return unused
        for i in range(len(unused)):
            lstCopy = unused[:]
            lstCopy.pop(i)
            subPerms = helper(lstCopy, perms)
            if len(subPerms) == 1:
                perms.append([i, subPerms])
            else:
                for l in subPerms:
                    perms.append([i] + l)
        return perms


print(Solution().getPermutation(2, 2)) # 213
print(Solution().getPermutation(4, 9)) # 2314
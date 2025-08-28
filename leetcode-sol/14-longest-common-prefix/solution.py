class Solution(object):
    def longestCommonPrefix(self, strs):
        # Sort the list of strings
        strs.sort()
        
        # Compare only the first and last strings after sorting
        x = strs[0]
        y = strs[-1]
        
        prefix = ""
        
        # Build prefix character by character
        for i in range(len(x)):
            if x[i] == y[i]:
                prefix += x[i]
            else:
                break
        
        return prefix

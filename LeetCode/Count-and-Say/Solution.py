class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        
        s = "1"
        for _ in range(2, n + 1):
            result = ""
            count = 1
            for i in range(1, len(s) + 1):
                if i < len(s) and s[i] == s[i - 1]:
                    count += 1
                else:
                    result += str(count) + s[i - 1]
                    count = 1
            s = result
        return s

class Solution:
    def isValid(self, s):
        if (len(s)%2 != 0) or (len(s)==0):
            return False
        openBrack = ''
        closeBrack = ''
        for i in s:
            print(i)
            if ((i=='(') or (i=='{') or (i=='[')):
                openBrack = openBrack + i
            elif ((i==')') or (i=='}') or (i==']')):
                closeBrack = closeBrack + i
        if len(openBrack) != len(closeBrack):
            return False
        print(openBrack)
        # closeBrack = closeBrack[::-1]
        print(closeBrack)
        return True
        

object1 = Solution()

print(object1.isValid('()[]{}({[]})'))
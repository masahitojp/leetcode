class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == ".*":
            return True
        elif "*" in p:
            a = 0
            for i in range(len(p)):
                if a >= len(s):
                    return False
                print(i, p[i], a, s[a])
                if p[i] == s[a]:
                    a = a + 1
                    pass
                elif p[i] == ".":
                    a = a + 1
                    pass
                elif p[i] == "*":
                    if a > 0 and p[i - 1] in s:
                        a = a + 1
                    pass
                elif i - 1 > 0 and p[i - 1] == "*" and p[i] != s[a]:
                    return False
                elif (i + 1) <= len(p) and p[i + 1] == "*":
                    pass
                else:
                    return False
            return True if (a > 0 and a == len(s)) else False
        else:
            if len(s) == len(p):
                for i in range(len(p)):
                    if p[i] == s[i]:
                        pass
                    elif p[i] == ".":
                        pass
                    else:
                        return False
                return True
            else:
                return False

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        assert 2 <= len(s) + len(t) and len(s) + len(t) <= 2*(5*10**4)
        assert str(type(s))=="<class 'str'>" and str(type(t))=="<class 'str'>" and (s == s.lower() and t == t.lower()) 
        if sorted(s)==sorted(t):
            return True
        return False



# print(str(type('koko'))=="<class 'str'>")
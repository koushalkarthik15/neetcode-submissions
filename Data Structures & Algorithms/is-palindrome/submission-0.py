class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        l=0
        r=n-1
        while l<r:
            while l<r and not ( ('a' <= s[l] <= 'z') or ('A' <= s[l] <= 'Z') or ('0' <= s[l] <= '9') ):
                l+=1
            while l<r and not ( ('a' <= s[r] <= 'z') or ('A' <= s[r] <= 'Z') or ('0' <= s[r] <= '9') ):
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True

        
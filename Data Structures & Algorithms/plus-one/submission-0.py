class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i=0
        first=1
        digits.reverse()
        while first:
            if i<len(digits):
                if digits[i]==9:
                    digits[i]=0
                else:
                    digits[i]+=1
                    first=0
            else:
                digits.append(first)
                first=0
            i+=1
        digits.reverse()
        return digits
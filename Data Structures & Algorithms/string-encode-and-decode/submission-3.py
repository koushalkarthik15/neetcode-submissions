class Solution:

    def encode(self, strs: List[str]) -> str:
        encode=""
        for word in strs:
            encode+=str(len(word))
            encode+='#'
            encode+=word
        return encode

    def decode(self, s: str) -> List[str]:
        i=0
        res=[]
        n=len(s)
        while i<n:
            length=0
            while s[i]!='#':
                length=length*10+int(s[i])
                i+=1
            i+=1
            word=""
            while length>0:
                word+=s[i]
                i+=1
                length-=1
            res.append(word)
        return res

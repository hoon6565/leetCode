class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()[::-1]
        reverseword = ""
        for word in s:
            reverseword += word + " "
        return reverseword[:-1]
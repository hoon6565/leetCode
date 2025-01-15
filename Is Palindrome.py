class Solution:
    def isPalindrome(self, s: str) -> bool:
        words = ""
        for word in s:
            if word.isalnum():
                words += word.lower()
        i = 0
        j = len(words)-1
        
        while i < j:
            if words[i] != words[j]:
                return False
            i += 1
            j -= 1
        return True
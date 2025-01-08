class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        reversed_string = s[::-1].strip()
        count = 0
        for c in reversed_string:
            if c == ' ':
                break
            count += 1
        return count
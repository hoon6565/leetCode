class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        splitList = []
        for word in words:
            replace = word.replace(separator," ")
            split = replace.split()
            splitList.extend(split)
        return splitList
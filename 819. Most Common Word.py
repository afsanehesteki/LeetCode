class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # str2 = paragraph.replace("!", " ").replace("?", " ").replace("'", " ").replace(",", " ").replace(";", " ").replace(":", " ").replace(".", " ")
        # arr = str2.lower().split()

        # instead of above bad practice
        remove="!?',;."
        for c in remove:
            paragraph=" ".join(paragraph.split(c))  
        paragraph = paragraph.lower().split()
        most_common = collections.Counter(arr).most_common()
        bannedset= set(banned)
        for word,_ in most_common:
            if word not in bannedset:
                return word

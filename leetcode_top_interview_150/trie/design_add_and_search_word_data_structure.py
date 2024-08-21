class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_last = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_last = True

    def search(self, word: str) -> bool:

        stk = [(self.root, 0)]

        while stk:
            cur, idx = stk.pop()
            if idx == len(word):
                if cur.is_last:
                    return True
                continue

            if word[idx] == ".":
                for c in cur.children:
                    stk.append((cur.children[c], idx + 1))
            elif word[idx] in cur.children:
                stk.append((cur.children[word[idx]], idx + 1))
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

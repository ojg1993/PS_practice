class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        0. remove repetition by converting data structure of word1 and word2 to set
        1. compare each set's elements are the same
        2. count each alphabet's repetition
        3. count the repetition hashmap values
        4. compare word1 count and word2 count
        """
        return set(word1) == set(word2) and Counter(Counter(word1).values()) == Counter(Counter(word2).values())

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        anagrams = []
        for word in words:
            if sorted(self.word) == sorted(word):
                anagrams.append(word)
        return anagrams

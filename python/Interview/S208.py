class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.x = {}
        self.p = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if word:
            self.x[word] = True
            for i in range(1,len(word)+1):
                self.p[word[0:i]] = True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

        for x in self.x:
            if word == x:
                return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return prefix in self.p



if __name__ == '__main__':
    s = Trie()
    s.insert("apple")
    print(s.search("apple"))
    print(s.startsWith("app"))
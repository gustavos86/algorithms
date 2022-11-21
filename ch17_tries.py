"""
Chapter 17
It Doesn't Hurt to Trie

Exercises
The following exercises provide you with the opportunity to practice with tries.
"""
class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def search(self, word):
        currentNode = self.root
    
        for char in word:
            # If the current node has child key with current character:​
            if currentNode.children.get(char):
                # Follow the child node:​
                currentNode = currentNode.children[char]
            else:
                # If the current character isn't found among​
                # the current node's children, our search word​
                # must not be in the trie:​
                return None
    
        return currentNode

    def insert(self, word):
        currentNode = self.root

        for char in word:
            # If the current node has child key with current character:​
            if currentNode.children.get(char):
                # Follow the child node:​
                currentNode = currentNode.children[char]
            else:
                # If the current character isn't found among​
                # the current node's children, we add​
                # the character as a new child node:​
                newNode = TrieNode()
                currentNode.children[char] = newNode

                # Follow this new node:​
                currentNode = newNode

        # After inserting the entire word into the trie,​
        # we add a * key at the end:​
        currentNode.children["*"] = None

    def traverse_and_print(self, node=None):
        """
        Write a function that traverses each node of a trie and prints each key, including all "*" keys.
        """
        if not node:
            currentNode = self.root
        else:
            currentNode = node


        for key, childNode in currentNode.children.items():
            print(key)

            if key != "*":
                self.traverse_and_print(childNode)

    def collectAllWords(self, node=None, word="", words=[]):
        # This method accepts three arguments. The first is the​
        # node whose descendants we're collecting words from.​
        # The second argument, word, begins as an empty string,​
        # and we add characters to it as we move through the trie.​
        # The third argument, words, begins as an empty array,​
        # and by the end of the function will contain all the words​
        # from the trie.
        # The current node is the node passed in as the first parameter,​
        # or the root node if none is provided:​
        currentNode = node or self.root 

        # We iterate through all the current node's children:​
        for key, childNode in currentNode.children.items():
            # If the current key is *, it means we hit the end of a​
            # complete word, so we can add it to our words array:​
            if key == "*":
                words.append(word)
            else: # If we're still in the middle of a word:​
                # We recursively call this function on the child node.​
                self.collectAllWords(childNode, word + key, words)

        return words

    def autocomplete(self, prefix):
        currentNode = self.search(prefix)
        if not currentNode:
            return None
        return self.collectAllWords(currentNode)

    def autocorrect(self, word):
        """
        Write an autocorrect function that attempts to replace a user's typo with a correct word.
        The function should accept a string that represents text a user typed in.
        If the user's string is not in the trie, the function should return an alternative word that shares the longest possible prefix with the user's string.

        For example, let's say our trie contained the words “cat,” “catnap,” and “catnip.”
        If the user accidentally types in “catnar,” our function should return “catnap,” since that's the word from the trie that shares the longest prefix with “catnar.”
        This is because both “catnar” and “catnap” share a prefix of “catna,” which is five characters long.
        The word “catnip” isn't as good, since it only shares the shorter, four-character prefix of “catn” with “catnar.”

        One more example: if the user types in “caxasfdij,” the function could return any of the words “cat,” “catnap,” and “catnip,”
        since they all share the same prefix of “ca” with the user's typo.

        If the user's string is found in the trie, the function should just return the word itself.
        This should be true even if the user's text is not a complete word, as we're only trying to correct typos, not suggest endings to the user's prefix.
        """
        currentNode = self.root
        # Keep track of how much of the user's word we've found 
        # in the trie so far. We'll need to concatenate this with
        # the best suffix we can find in the trie.
        wordFoundSoFar = ""

        for char in word:
            # If the current node has child key with current character:
            if currentNode.children.get(char): 
                wordFoundSoFar += char 
                # Follow the child node:    
                currentNode = currentNode.children.get(char)
            else:
                # If the current character isn't found among
                # the current node's children, collect all the suffixes that 
                # descend from the current node and get the first one.
                # We concatenate the suffix with the prefix we've found so
                # far to suggest the word the user meant to type in:
                return wordFoundSoFar + self.collectAllWords(currentNode)[0]

        # If the user's word is found in the trie:
        return word

trie = Trie()
trie.insert("cat")
trie.insert("dog")
trie.insert("got")
trie.insert("gotten")
trie.traverse_and_print()

word = "catasdf"
suggestion = trie.autocorrect(word)
print(f"For word {word} the suggestion is {suggestion}")
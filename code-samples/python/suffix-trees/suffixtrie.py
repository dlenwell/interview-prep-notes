"""
Suffix trie data structure

This structure allows for quickly answering the following types of queries:

has sub string

has suffix

number of times a sub string

cons:
 super linier growth
 quatratic space

"""


class SuffixTrie(object):

    def __init__(self, string):
        """
        Make suffix trie as a dictionary object from string
        """
        self.string = string
        string += '$'  # special terminator symbol
        self.root = {}

        for index in range(len(string)):  # for each suffix
            current = self.root

            for character in string[index:]:
                # for each character in idexed'th suffix
                if character not in current:
                    current[character] = {}
                    # add outgoing edge if necessary
                current = current[character]

    def follow_path(self, string):
        """
        Follow path given by characters of string.

        Return node at end of path, or None if we fall off.
        """
        current = self.root

        for character in string:
            if character not in current:
                return(None)

            current = current[character]

        return(current)

    def has(self, string):
        """
        Return true if string appears as a substring of self.root
        """
        return(self.follow_path(string) is not None)

    def has_suffix(self, string):
        """
        Return true if string is a suffix of self.string
        """
        node = self.follow_path(string)

        if node is not None and '$' not in node:
            return(False)

        return True

    def number_of_unuiqe(self, string):
        """
        returns an integer that should match the number of times a substring
        shows up.
        """
        node = self.follow_path(string)

        return(len(node))


if __name__ == "__main__":
    string = 'The fox was a fox3 quick brown fox!'

    trie = SuffixTrie(string)

    print()
    print("string:", string)
    print()
    print("trie.has('quick') : {}".format(trie.has('quick')))
    print("trie.has('fax') : {}".format(trie.has('fax')))
    print()
    print()
    print("trie.has_suffix('the') : {}".format(trie.has_suffix('the')))
    print("trie.has_suffix('The') : {}".format(trie.has_suffix('The')))
    print("trie.has_suffix('fox!') : {}".format(trie.has_suffix('fox!')))
    print()
    print()

    print("trie.number_of_unuiqe('fox') : {}".format(
        trie.number_of_unuiqe('fox')
    ))
    print("trie.number_of_unuiqe('quick') : {}".format(
        trie.number_of_unuiqe('quick')
    ))

"""
leedcode problem: 
    https://leetcode.com/problems/word-pattern/description/

    Given a pattern and a string s, find if s follows the same pattern.
    
    Here follow means a full match, such that there is a bijection between a letter
    in pattern and a non-empty word in s. Specifically:

    Each letter in pattern maps to exactly one unique word in s.
    Each unique word in s maps to exactly one letter in pattern.
    No two letters map to the same word, and no two words map to the same letter.
"""
from inputs import scenarios


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        word pattern matching function
        Parameters:
        pattern (string): pattern to follow
        s (string): string with words we are testing for the pattern

        Returns:
        bool:Returning
        """
        pattern_map = {}
        words = s.split()
        already_mapped = set()

        for index, char in enumerate(pattern):
            if len(words) <= index: # this triggers when we find a pattern demand but the word index isn't long enough to meet it
                return False
            if char not in pattern_map: # first encounter of letter in pattern, save it to index
                if words[index] in already_mapped: # catch if the value was alraedy inputted for another char
                    return False
                already_mapped.add(words[index])
                pattern_map[char] = words[index]
            else: # its already in the dictionary, we need to see if the word matches the established pattern
                if pattern_map[char] != words[index]:
                    return False
        return True


def main():
    """
    main exercise run through...
    """
    solution = Solution()

    print()
    print("===================================")
    print()
    print("Running scenarios:")
    
    for scenario in scenarios:
        
        print("pattern: ", scenario["pattern"])
        print("string: ", scenario["data"])
        print("expected result:", scenario["assert"])
        actual = solution.wordPattern(scenario["pattern"], scenario["data"])
        print("result: ", actual)
        if scenario["assert"] == actual:
            print("PASSED!")
        else:
            print("FAILED!")

        print()
        print("===================================")

if __name__ == "__main__":
    """
    triggered when file is executed, ignored when included
    """
    main()
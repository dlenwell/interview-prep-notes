"""
leedcode problem: group-anagrams 
    https://leetcode.com/problems/group-anagrams/description/?utm_source=chatgpt.com

    Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""
from collections import Counter

from inputs import normalize, scenarios_dup, scenarios_no_dup


class Solution:
    def groupAnagramsOptimized(self, words: list[str]) -> list[list[str]]:
        """
        groupAnagramsOptimized

        does preserve duplicate words.

        Parameters:
        words (string): input list of words
        
        Returns:
        list: groupped anagrams in lists 
        """
        mapped_dict = {}

        for word in words:
            sword = ''.join(sorted(word))

            if sword not in mapped_dict: 
                mapped_dict[sword] = []

            mapped_dict[sword].append(word)

        return list(mapped_dict.values())
    
    def groupAnagramsCounter_nodup(self, words: list[str]) -> list[list[str]]:
        """
        groupAnagramsCounter_nodup

        does not preserve duplicate words.

        Parameters:
        words (string): input list of words
        
        Returns:
        list: groupped anagrams in lists 
        """
        grouped = []
        added_words = set()
        
        for word in words:
            # first is the word already in a grouped list?
            if word not in added_words: # if not, we can test it to see if the following words match
                added_words.add(word)
                word_anagrams = [word,]
                rest_of_words = words.copy()
                rest_of_words.remove(word)
                for rest in rest_of_words:
                    if rest not in added_words and Counter(word) == Counter(rest):
                        added_words.add(rest)
                        word_anagrams.append(rest)
                         
                grouped.append(word_anagrams)
             
        return grouped
    
    def groupAnagramsCounter_preservedup(self, words: list[str]) -> list[list[str]]:
        """
        groupAnagramsCounter_nodup

        does preserve duplicate words.

        Parameters:
        words (string): input list of words
        
        Returns:
        list: groupped anagrams in lists 
        """
        grouped = []
        
        for index, word in enumerate(words):
            # first is the word already in a grouped list?
            if not any(word in sublist for sublist in grouped):
                word_anagrams = [word,]
                rest_of_words = words.copy()
                rest_of_words.pop(index)
                for rest in rest_of_words:
                    if Counter(rest) == Counter(word):
                        word_anagrams.append(rest)
                grouped.append(word_anagrams)

        return grouped

    def groupAnagramsSorted(self, words: list[str]) -> list[list[str]]:
        """
        groupAnagramsSorted

        does preserve duplicate words. And uses sorted function rather than Counter to avoid imports.

        Parameters:
        words (string): input list of words
        
        Returns:
        list: groupped anagrams in lists 
        """
        grouped = []
        added_words = set()

        for word in words:
            # first is the word already in a grouped list?
            if word not in added_words: # if not, we can test it to see if the following words match
                added_words.add(word)
                word_anagrams = [word,]
                rest_of_words = words.copy()
                rest_of_words.remove(word)
                for rest in rest_of_words:
                    if rest not in added_words and sorted(word) == sorted(rest):
                        added_words.add(rest)
                        word_anagrams.append(rest)
                        
                grouped.append(word_anagrams)
            
        return grouped

def main():
    """
    main exercise run through...
    """
    solution = Solution()

    

    print()
    print("===================================")
    print()
    print("Running optimized version:")
    
    for scenario1 in scenarios_dup:
            
        print("input: ", scenario1["data"])
        print("expected result:", scenario1["assert"])
        actual = solution.groupAnagramsOptimized(scenario1["data"])
        print("result: ", actual)
        if normalize(scenario1["assert"]) == normalize(actual):
            print("PASSED!")
        else:
            print("FAILED!")
    
        print()
        print("===================================")


    
    print()
    print("===================================")
    print()
    print("Running Counter with dups scenarios:")
    
    for scenario1 in scenarios_dup:
            
        print("input: ", scenario1["data"])
        print("expected result:", scenario1["assert"])
        actual = solution.groupAnagramsCounter_preservedup(scenario1["data"])
        print("result: ", actual)
        if normalize(scenario1["assert"]) == normalize(actual):
            print("PASSED!")
        else:
            print("FAILED!")
    
        print()
        print("===================================")

    
    
    print()
    print("Running counter no dup scenarios:")

    for scenario_nodup in scenarios_no_dup:
        
        print("input: ", scenario_nodup["data"])
        print("expected result:", scenario_nodup["assert"])
        thisactual = solution.groupAnagramsCounter_nodup(scenario_nodup["data"])
        print("result: ", thisactual)
        if normalize(scenario_nodup["assert"]) == normalize(thisactual):
            print("PASSED!")
        else:
            print("FAILED!")
    
        print()
        print("===================================")

        print()

    print("Running sorted (slower) scenarios:")

    for scenario_nodup in scenarios_no_dup:
        
        print("input: ", scenario_nodup["data"])
        print("expected result:", scenario_nodup["assert"])
        thisactual = solution.groupAnagramsSorted(scenario_nodup["data"])
        print("result: ", thisactual)
        if normalize(scenario_nodup["assert"]) == normalize(thisactual):
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
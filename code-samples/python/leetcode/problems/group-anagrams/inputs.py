"""
shared data set for test harnes and functional tests
"""

scenarios_dup = [
    {
        'data': ["eat","tea","tan","ate","nat","bat","eat"],
        'assert': [["bat"],["nat","tan"],["ate","eat","eat","tea"]]
    },
    {
        'data': ["eat", "tea", "eat", "ate", "dog", "god"],
        'assert': [["eat", "tea", "eat", "ate"],["dog", "god"]]
    },
    {
        'data': ["eat", "tea", "ate", "tea"],
        'assert': [["eat", "tea", "ate", "tea"]]
    },
    {
        'data': [""],
        'assert': [[""]]
    },
    {
        'data': ["a"],
        'assert': [["a"]]
    },
]

scenarios_no_dup = [
    {
        'data': ["eat","tea","tan","ate","nat","bat"],
        'assert': [["bat"],["nat","tan"],["ate","eat","tea"]]
    },

    {
        'data': ["eat", "tea", "eat", "ate", "dog", "god"],
        'assert': [["eat", "tea", "ate"],["dog", "god"]]
    },
    {
        'data': ["eat", "tea", "tea"],
        'assert': [["eat", "tea"]]
    },
    {
        'data': [""],
        'assert': [[""]]
    },
    {
        'data': ["a"],
        'assert': [["a"]]
    },
]

def normalize(groups):
    """
    normalizes list for fast comparisons 
    """
    return sorted(tuple(sorted(group)) for group in groups)
"""
shared data set for test harnes and functional tests
"""

scenarios = [
    {
        'pattern': "abab",
        'data': "cat dog cat dog",
        'assert': True
    },
    {
        'pattern': "abab",
        'data': "cat dog cat fish",
        'assert': False
    },
    {
        "pattern": "abc",
        "data": "cat dog",
        "assert": False
    },
    {
        "pattern": "ab",
        "data": "cat cat",
        "assert": False
    },
    {
        "pattern": "aba",
        "data": "cat dog",
        "assert": False
    }
]
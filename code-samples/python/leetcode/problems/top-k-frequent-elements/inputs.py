"""
shared data set for test harnes and functional tests
"""

scenarios = [
    {
        'k': 2,
        'nums': [1,3,3,2,2,3,7,7,7,7,7,7,7,7,7,23],
        'assert': [7,3]
    },
    {
        'k': 1,
        'nums': [1],
        'assert': [1]
    },
    {
        'k': 2,
        'nums': [1,2,1,2,1,2,3,1,3,2],
        'assert': [1,2]
    },
]

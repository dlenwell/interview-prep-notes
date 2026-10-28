"""
leedcode problem: 
    https://leetcode.com/problems/top-k-frequent-elements/description/

    Given an integer array nums and an integer k, return the k most frequent elements.
    You may return the answer in any order.
"""
from collections import Counter

from inputs import scenarios


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        returns most reoccuring integers in num, 
        limits response by k
        
        Parameters:
        nums (list[int]): data to parse
        k (int): number of leaders to return

        Returns:
        list[int]: Returning list of integers
        """
        pattern_map = {}

        for num in nums:
            if num not in pattern_map:
                pattern_map[num] = 0
            pattern_map[num] += 1

        sorted_dict = dict(sorted(pattern_map.items(), key=lambda item: item[1], reverse=True))

        return list(sorted_dict.keys())[0:k]

    def topKFrequentoptimized(self, nums: list[int], k: int) -> list[int]:
        """
        returns most reoccuring integers in num, 
        limits response by k
        
        Parameters:
        nums (list[int]): data to parse
        k (int): number of leaders to return

        Returns:
        list[int]: Returning list of integers
        """
        cnums = Counter(nums)

        groups = [[] for _ in range(len(nums) + 1)]

        for num, count in cnums.items():
            groups[count].append(num)

        result = []
        
        for index in range(len(groups) - 1, 0, -1):
            for num in groups[index]:
                result.append(num)
                if len(result) == k:
                    return result


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
        
        print("nums: ", scenario["nums"])
        print("k: ", scenario["k"])
        print("expected result:", scenario["assert"])
        actual = solution.topKFrequentoptimized(scenario["nums"], scenario["k"])
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
"""
sliding window example
"""


def longest_sub_string(data):
    """
    returns the length of the longest unuiqe substring

    complexity: o(n)

    """
    # pointers
    pointer_1 = 0
    pointer_2 = 0
    longest = 0
    pocket = []

    # outer loop moves pointer_1
    while pointer_1 < len(data):
        character = data[pointer_1]

        # inner loop moves pointer_2
        while character in pocket:
            pocket.remove(character)
            pointer_2 += 1

        pocket.append(character)
        longest = max(longest, pointer_1 - pointer_2 + 1)
        pointer_1 += 1

    return(longest)


def min_sub_string(haystack, needles):
    """
    returns the minimim substring that has all characters in the needles input

    complexity:  o(n+m)
    """
    # pointers
    left = 0
    right = 0

    # create a map of the needle string
    map = {}
    for character in needles:
        map[character] = 1

    # minimum found length
    shortest = len(haystack)
    count = len(needles)
    # default return value if subsring isn't present
    found = None

    # outer loop moves the right pointer
    while right < len(haystack):
        right_character = haystack[right]
        right += 1

        # if the right_character is in our
        if right_character in map.keys():
            map[right_character] -= 1
            if map[right_character] == 0:
                count -= 1

        # inner loop moves the left pointer
        while count == 0:
            left_character = haystack[left]
            left += 1
            if left_character in map.keys():
                map[left_character] += 1
                if map[left_character] > 0:
                    count += 1

            # if we make it this far it means we found the thing
            if (right - left) < shortest:
                # decide if this is the shortest one we found
                shortest = (right - left)
                found = haystack[left-1:right]

    return(found)


def main():
    haystack = "this is a string"
    needle = "hn"
    print("min_sub_string -> ", min_sub_string(haystack, needle))

    print("longest_sub_string('WEREWSDESSEDTEEWSSE') -> ",
          longest_sub_string('WEREWSDESSEDTEEWSSE'))

    print("longest_sub_string('WEWERWERWERWEDJJDMUSHHENREWSDESSEDTEEWSS') -> ",
          longest_sub_string('WEWERWERWERWEDJJDMUSHHENREWSDESSEDTEEWSS'))


if __name__ == "__main__":
    """
    """
    main()

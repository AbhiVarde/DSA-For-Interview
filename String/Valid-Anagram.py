# We sort both strings and compare them. If the sorted versions are equal,
# then the strings are anagrams of each other.


def isAnagram(s, t):
    return sorted(s) == sorted(t)

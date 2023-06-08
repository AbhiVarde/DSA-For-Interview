# To group anagrams together, we sort the characters of each word and use the sorted word as a key in a dictionary. We append each word to the list associated with the key. Finally, we return the values of the dictionary as a list. This allows us to efficiently group the anagrams without using extensive code.

def groupAnagrams(strs):
    groups = {}
    for word in strs:
        sorted_word = ''.join(sorted(word))
        groups.setdefault(sorted_word, []).append(word)
    return list(groups.values())

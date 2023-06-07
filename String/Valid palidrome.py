# We use regular expressions (re.sub) to remove all non-alphanumeric characters from the string. We convert
# the resulting string to lowercase and check if it is equal to its reverse.

import re


def isPalindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return s == s[::-1]

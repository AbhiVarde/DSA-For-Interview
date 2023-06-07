# We split the string into words using the split() method, reverse the order of the resulting list,
# and join the words back together using the join() method.

def reverseWords(s):
    return ' '.join(s.split()[::-1])

# Using a stack, iterate through the characters.
# Remove duplicates by comparing the current character with the top of the stack.
# Append non-duplicates to the stack. Return the stack as a string.

def removeDuplicates(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

"""
We are given a string s, we need to find the count of all contiguous substrings starting and ending with the same character.
Sample Input 1: s = "abcab"
Sample Output 1: 7
"""
count = 0
def printSubstring(str, start, end):
    if start == end:
        return

    if str[start] == str[end-1]:
        print(str[start: end])

    printSubstring(str, start + 1, end)
    printSubstring(str, start, end - 1)

printSubstring("abcab", 0, 5)
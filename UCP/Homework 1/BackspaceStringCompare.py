#Given two strings representing series of keystrokes, determine whether the resulting text is the same. Backspaces are represented by the '#' character so "x#" results in the empty string ("").

def decodeWord(string: str) -> str:
    if not string:
        return []
    
    stack = []
    
    for letter in string:
        if letter == "#" and stack:
            stack.pop()
        else:
            stack.append(letter)
    
    return "".join(stack)

def backspaceStringCompare(string1: str, string2: str) -> bool:
    decodedString1 = decodeWord(string1)
    decodedString2 = decodeWord(string2)
    
    return decodedString1 == decodedString2

word1 = "abcde"
word2 = "abcde"
print(backspaceStringCompare(word1, word2))

word1 = "abcdef###xyz"
word2 = "abcw#xyz"
print(backspaceStringCompare(word1, word2))

word1 = "Uber Career Prep"
word2 = "u#Uber Careee#r Prep"
print(backspaceStringCompare(word1, word2))

word1 = "abcdef###xyz"
word2 = "abcdefxyz###"
print(backspaceStringCompare(word1, word2))


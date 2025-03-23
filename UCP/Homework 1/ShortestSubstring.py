#Given a string and a second string representing required characters, return the length of the shortest substring containing all the required characters.

def shortestSubstring(word1: str, word2: str) -> int:
    
    requiredWindow = {}
    for letter in word2:
        requiredWindow[letter] = requiredWindow.get(letter, 0) + 1
    requiredMatches = len(requiredWindow)
    
    currentWindow = {}
    currentMatches = 0
    left, right, ans = 0, 0, float("inf")
    
    while right < len(word1):
        curLetter = word1[right]
        currentWindow[curLetter] = currentWindow.get(curLetter, 0) + 1
        
        if curLetter in requiredWindow and currentWindow[curLetter] == requiredWindow[curLetter]:
            currentMatches += 1
        
        while currentMatches == requiredMatches:
            ans = min(ans, right - left + 1)
            letterToRemove = word1[left]
            currentWindow[letterToRemove] -= 1
            
            if letterToRemove in requiredWindow and currentWindow[letterToRemove] < requiredWindow[letterToRemove]:
                currentMatches -= 1
            
            left += 1    
        
        right += 1
    
    return int(ans)


word1 = "abracadabra"
word2 = "abc"
print(shortestSubstring(word1, word2))

word1 = "zxycbaabcdwxyzzxwdcbxyzabccbazyx"
word2 = "zzyzx"
print(shortestSubstring(word1, word2))

word1 = "dog"
word2 = "god"
print(shortestSubstring(word1, word2))

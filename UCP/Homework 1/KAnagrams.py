def kAnagrams(s1: str, s2: str, k : int) -> bool:
    if len(s1) != len(s2):
        return False
    
    # Remove spaces for strings like "debit curd" and "bad credit"
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")
    
    # If lengths are still different after removing spaces, they can't be k-anagrams
    if len(s1) != len(s2):
        return False
    
    # Count characters in first string
    char_count = {}
    for char in s1:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Subtract characters from second string
    for char in s2:
        char_count[char] = char_count.get(char, 0) - 1
    
    # Count how many characters need to be changed
    # This is the sum of all positive values in char_count
    # (or alternatively, the sum of all negative values)
    differences = sum(abs(count) for count in char_count.values()) // 2
    
    # If differences <= k, we can make them anagrams by changing at most k chars
    return differences <= k


word1 = "apple"
word2 = "peach"
print(kAnagrams(word1, word2, 1))

print(kAnagrams(word1, word2, 2))

word1 = "cat"
word2 = "dog"
print(kAnagrams(word1, word2, 3))

word1 = "debit curd"
word2 = "bad credit"
print(kAnagrams(word1, word2, 1))

word1 = "baseball"
word2 = "basketball"
print(kAnagrams(word1, word2, 2))


print(kAnagrams("anagram", "mangaar", 2))

word1 = "fodr"
word2 = "grok"
print(kAnagrams(word1, word2, 2))
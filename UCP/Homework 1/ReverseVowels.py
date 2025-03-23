#Given a word, reverse the order of the vowels in the word.

def reverseVowels(string: str) -> str:
    if not string:
        return None
    
    word = list(string)
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    
    left, right = 0, len(word) - 1
    
    while left < right:
        while left < right and word[left] not in vowels:
            left += 1
        while left < right and word[right] not in vowels:
            right -= 1
        
        word[left], word[right] = word[right], word[left]
        left += 1
        right -= 1
    
    return "".join(word)    
    


word = "Uber Career Prep"
word = "flamingo"
print(reverseVowels(word))
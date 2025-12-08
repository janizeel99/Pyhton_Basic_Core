def longest_word_with_vowel(words):
    vowels = set('aeiouAEIOU')

    word_with_vowel = [w for w in words if any(char in vowels for char in w)]

    if not word_with_vowel:
        return None 
    
    word_with_vowel.sort(key=lambda w: (-len(w), w))


    return word_with_vowel[0]


words = ["sky", "orange", "blue", "rhythm", "banana"]  
result = longest_word_with_vowel(words)
print(result)
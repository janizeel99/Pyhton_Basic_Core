import string

def word_frequency(text, exclude_words=None):
    text = text.lower()

    
    for p in string.punctuation:
        text = text.replace(p, "")


    words = text.split()

    exclude_set = set(word.lower() for word in exclude_words) if exclude_words else set()

    frequency = {}

    for word in words:
        if word not in exclude_set:
            frequency[word] = frequency.get(word, 0) + 1

    return frequency


input_string = "Apple, apple, orange!! banana, apple orange?"
exclude = ["orange"]

result = word_frequency(input_string, exclude)
print(result)

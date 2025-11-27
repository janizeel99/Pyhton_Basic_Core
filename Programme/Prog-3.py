def char_frequency(text):
    # Convert to lowercase and remove spaces
    text = text.replace(" ", "").lower()
    
    freq = {}

    # Count frequency of each character
    for char in text:
        freq[char] = freq.get(char, 0) + 1

    # Sort dictionary by frequency (descending)
    sorted_freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
    
    return sorted_freq

# Example
input_string = "Hello World"
print(char_frequency(input_string))
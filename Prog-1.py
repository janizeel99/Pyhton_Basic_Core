import re

def process_string(text):
    
    numbers = re.findall(r'\d+', text)
    

    nums = list(map(int, numbers))
    
    # Calculate sum
    total_sum = sum(nums)
    
    
    def replace_with_square(match):
        num = int(match.group())
        return str(num * num)
    
    
    modified_text = re.sub(r'\d+', replace_with_square, text)
    
    return total_sum, modified_text

Input_data = "The house number is 12, and the cost of renovation was 150 dollars"
result_sum, result_string = process_string(Input_data)

print("Sum of numbers:", result_sum)
print("Modified string:", result_string)
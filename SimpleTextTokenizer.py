import re
text = "This is a simple text tokenizer. It will split the text into tokens based on whitespace and punctuation."
res = re.split(r'(\s)' , text )
print(res)
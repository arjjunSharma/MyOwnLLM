import re
class SimpleTokenizer1:
    def __init__(self , vocab):
        self.str_to_int = vocab
        self.int_to_str = {i:s for s, i in vocab.items()}
    def encode(self, text):
        preprocessed_text = re.split(r'([,.;:?_!()\']|--|\s)', text )
        preprocessed_text= [item.strip() for item in preprocessed_text if item.strip()]
        ids = [self.str_to_int[s] for s in preprocessed_text]
        return ids
    def decode(self , ids):
        text = " ".join(self.int_to_str[i] for i in ids)
        text = re.sub(r'\s([,.;:?_!()\']|--)\s', r'\1', text)
        return text
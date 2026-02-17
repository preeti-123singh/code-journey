import re

def extract_keywords(text):
    # simple cleaning
    words = re.findall(r'\b[a-zA-Z]{3,}\b', text)
    common_words = {"and", "the", "for", "with", "you", "your", "are", "from"}
    return [w for w in words if w not in common_words]

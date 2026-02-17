def parse_jd(jd_text):
    """Return a list of unique words from the job description"""
    words = set(jd_text.lower().split())
    return words

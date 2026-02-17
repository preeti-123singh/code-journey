def calculate_match(resume_text, jd_text):
    """Calculate match percentage and keywords"""
    resume_words = set(resume_text.split())
    jd_words = set(jd_text.split())

    matching = resume_words & jd_words
    missing = jd_words - resume_words

    match_percentage = int(len(matching) / len(jd_words) * 100) if jd_words else 0

    future_suggestions = ""
    if match_percentage < 100:
        future_suggestions = f"Learn missing skills: {', '.join(list(missing)[:5])}..."

    return {
        'match_percentage': match_percentage,
        'matching_keywords': list(matching),
        'missing_keywords': list(missing),
        'future_suggestions': future_suggestions
    }

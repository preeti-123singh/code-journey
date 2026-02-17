def generate_suggestions(missing_keywords):
    if not missing_keywords:
        return ["Excellent! Your resume already matches most of the job description."]
    suggestions = [
        f"Consider adding skills or experience related to: {', '.join(missing_keywords[:5])}.",
        "Include measurable achievements or relevant certifications in those areas."
    ]
    return suggestions

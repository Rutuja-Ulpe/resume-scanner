SKILLS = [
    "python", "sql", "machine learning", "deep learning",
    "nlp", "pandas", "numpy", "scikit learn",
    "data analysis", "statistics"
]

def extract_skills(text):
    found_skills = []
    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)
    return found_skills

def solution(table, languages, preference):
    pref_dic = {"JAVA": 0, "JAVASCRIPT": 0, "C": 0, "C++": 0, "C#": 0, "SQL": 0, "PYTHON": 0, "KOTLIN": 0, "PHP": 0}
    for language, preference in zip(languages, preference):
        pref_dic[language] = preference

    industry, max_score = '', 0
    for info in table:
        temp = info.split()
        field, response = temp[0], temp[1:]
        score = 0
        for idx, lang in enumerate(response):
            score += pref_dic[lang] * (5 - idx)
        if max_score < score:
            max_score = score
            industry = field
        elif max_score == score and ord(industry[0]) > ord(field[0]):
            industry = field
    return industry
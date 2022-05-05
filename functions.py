import string


def clear_punctuation(content: str):
    """
    Функция удаляет все знаки препинания из строки
    """
    punctuation = string.punctuation
    for i in punctuation:
        if i in content:
            content = content.replace(i, '')
    return content

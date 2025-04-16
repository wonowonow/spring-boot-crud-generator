def get_input(prompt, default=None):
    if default:
        result = input(f"{prompt} [{default}]: \n> ")
        return result if result else default
    return input(f"{prompt}: \n> ")

def get_plural(word):
    """단어의 복수형을 반환합니다."""
    if word.endswith('y'):
        return word[:-1] + 'ies'
    elif word.endswith(('s', 'x', 'z', 'ch', 'sh')):
        return word + 'es'
    else:
        return word + 's'

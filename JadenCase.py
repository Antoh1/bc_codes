def toJadenCase(string):
    """this function converts a given string so that every word start with a cap"""
    if string == "" or None:
        return null
    split_str = string.split(' ')
    str_output = []
    for word in split_str:
        word_result = word.capitalize()
        str_output.append(word_result)
    final_result = ' '.join(str_output)

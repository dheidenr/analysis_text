import operator


def common_words(file_name, items):
    """
    Функция возвращающая количество частво встречающихся слов в файле
    :param file_name:
    :param items:
    :return:
    """
    words_map = dict()
    with open(file_name, 'r', encoding='utf-8') as text:
        for line in text.readlines():
            for word in line.split():
                cleaned_word = word.strip('.,!-').lower()
                if cleaned_word not in words_map:
                    words_map[cleaned_word] = 0
                words_map[cleaned_word] += 1
    words_items = words_map.items()
    word_count_items = sorted(words_items, key=operator.itemgetter(1),
                              reverse=True)
    return word_count_items[:items]

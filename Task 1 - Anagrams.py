def reverse_text(text):
    words = text.split(' ')
    return ' '.join(reverse_word(i) for i in words)


def reverse_word(word):
    numbers = []
    wrong_letter = []
    letters = []
    for count, letter in enumerate(word):
        if not letter.isalpha():
            wrong_letter.append(letter)
            numbers.append(count)
        else:
            letters.append(letter)

    letters.reverse()

    for i in range(0, len(numbers)):
        letters.insert(numbers[i], wrong_letter[i])

    return ''.join(i for i in letters)


if __name__ == '__main__':
    cases = [
        ('abcd efgh', 'dcba hgfe'),
        ('akbcd efg!h', 'dcbka hgf!e'),
        ('', ''),
        ('a', 'a'),
        (' ', ' '),
        ("your funct10n shou1d  work on @ny amount of w0rd5  and other  Ch@r@cter5",
         "ruoy ntcnu10f duoh1s  krow no @yn tnuoma fo d0rw5  dna rehto  re@t@crhC5"),
    ]

    for text, reversed_text in cases:
        assert reverse_text(text) == reversed_text

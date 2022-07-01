def split_text(main):
    words = main.split(' ')
    new_text = []
    for i in words:
        new_text.append(reverse(i))
    new_text = " ".join(new_text)
    return new_text


def reverse(word):
    count = 0
    numbers = []
    wrong_letter = []

    for letter in word:
        count += 1
        if not letter.isalpha():
            word = word.replace(letter, '')
            wrong_letter.append(letter)
            numbers.append(count)

    word = word[::-1]

    for i in range(0, len(numbers)):
        word = word[:numbers[i] - 1] + wrong_letter[i] + word[numbers[i] - 1::]

    return word


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
        assert split_text(text) == reversed_text

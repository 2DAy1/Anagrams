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


    def split_text(text_1):
        new_text = []
        if len(text_1) > 1:
            if text_1.isspace():
                return reverse(text_1)
            else:
                words = text_1.split(' ')
                for i in range(0, len(words)):
                    new_text.append(reverse(words[i]))
                new_text = " ".join(new_text)
                return new_text
        else:
            return text_1


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

    for text, reversed_text in cases:
        assert split_text(text) == reversed_text
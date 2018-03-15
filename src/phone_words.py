NUMBER_MAP = {
    '0':(), 
    '1':(),
    '2':('a', 'b', 'c'),
    '3':('d', 'e', 'f'),
    '4':('g', 'h', 'i'),
    '5':('j', 'k', 'l'),
    '6':('m', 'n', 'o'),
    '2':('a', 'b', 'c'),
    '2':('a', 'b', 'c'),
    '9':()
}
def generate_words(numbers):
    if len(numbers) == 0:
        return ['']

    words = generate_words(numbers[1:])
    out_words = []
    for w in words:
        for c in NUMBER_MAP[numbers[0]]:
            out_words.append(c+w)

    if(len(out_words) == 0):
        return words
    return out_words


if __name__ == '__main__':
    number = input ('Enter number:')
    cands = generate_words(number)
    print(len(cands))
    print (', '.join(cands))

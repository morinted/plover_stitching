def stitch_word(word, delimiter='-'):
    return ' '.join(
        [delimiter.join(list(word)) for word in word.split(' ')]
    )

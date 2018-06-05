from plover.formatting import WORD_RX

def stitch_word(word, delimiter='-'):
    text = ''
    words = WORD_RX.findall(word)
    for w in words:
        sw = w.rstrip()
        text += delimiter.join(w.rstrip()) + w[len(sw):]
    return text
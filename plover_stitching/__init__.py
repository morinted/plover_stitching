def _stitch_word(word, delimiter='-'):
    return ' '.join(
        [delimiter.join(list(word)) for word in word.split(' ')]
    )

def stitch(ctx, cmdline):
    # Placeholder
    action = ctx.copy_last_action()
    result = None
    if result:
        emoji, phrase = result
        action.text = emoji
        action.prev_replace = ''.join(phrase)
        action.prev_attach = True
        action.word = None
    return action

def stitch_last_word(ctx, cmdline):
    # Placeholder
    action = ctx.copy_last_action()
    result = None
    if result:
        emoji, phrase = result
        action.text = emoji
        action.prev_replace = ''.join(phrase)
        action.prev_attach = True
        action.word = None
    return action

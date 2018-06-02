from plover_stitching.stitching import stitch_word

def stitch(ctx, cmdline):
    action = ctx.copy_last_action()
    # {:stitch:word:delimiter?}
    # E.g. {:stitch:A} {:stitch:B:~}
    args = cmdline.split(':')
    try:
        word = args[0]
    except IndexError:
        # A word was not provided
        return action
    try:
        delimiter = args[1]
    except IndexError:
        # Optional delimiter not provided, default to hyphen
        delimiter = '-'

    action = ctx.new_action()
    action.prev_attach = ctx.last_action.glue or ctx.last_action.next_attach
    action.glue = True
    action.text = delimiter + word if ctx.last_action.glue else word

    return action

def stitch_last_word(ctx, cmdline):
    args = cmdline.split(':')
    try:
        if args[0]:
            num_words_to_stitch = int(args[0])
        else:
            num_words_to_stitch = 1
    except IndexError:
        num_words_to_stitch = 1
    try:
        delimiter = args[1]
    except IndexError:
        # Optional delimiter not provided, default to hyphen
        delimiter = '-'

    action = ctx.copy_last_action()

    last_words = "".join(ctx.last_words(count=num_words_to_stitch))
    if last_words:
        action.text = stitch_word(last_words, delimiter=delimiter)
        action.prev_replace = last_words
        action.prev_attach = True
        action.word = None

    return action


from plover_stitching.stitching import (
    stitch_word
)

def test_stitch_word():
    assert stitch_word(' testing ') == 't-e-s-t-i-n-g '
    assert stitch_word('have you got   ') == 'h-a-v-e y-o-u g-o-t   '
    assert stitch_word('have you got   ', delimiter='👏') == 'h👏a👏v👏e y👏o👏u g👏o👏t   '
    assert stitch_word('will\nyou\n') == 'w-i-l-l\ny-o-u\n'

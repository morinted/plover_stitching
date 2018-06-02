
from plover_stitching import (
    _stitch_word
)

def test_stitch_word():
    assert _stitch_word(' testing ') == ' t-e-s-t-i-n-g '
    assert _stitch_word('have you got   ') == 'h-a-v-e y-o-u g-o-t   '
    assert _stitch_word('have you got   ', delimiter='👏') == 'h👏a👏v👏e y👏o👏u g👏o👏t   '

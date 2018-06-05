from plover_build_utils.testing import BlackboxTester
from plover.registry import registry
from plover import system

class TestsBlackbox(BlackboxTester):

    @classmethod
    def setup_class(cls):
        super().setup_class()
        registry.update()
        system.setup('English Stenotype')

    def test_stitch_last_word(self):
        r'''
        "TEFT": "test",
        "S": "{:stitch_last_word}",

        TEFT/S  " t-e-s-t"
        '''

    def test_stitch_last_word_nonword(self):
        r'''
        "TEFT": "test",
        "KW-BG": "{,}",
        "PHE": "me",
        "S": "{:stitch_last_word:3}",

        TEFT/KW-BG/PHE/S  " t-e-s-t, m-e"
        '''

    def test_stitch_fingerspelling(self):
        r'''
        "A": "{:stitch:A}",
        "PW": "{:stitch:B}",
        "KR": "{:stitch:C}",
        "KW-BG": "{,}",

        A             ' A'
        PW/KR         ' A-B-C'
        *             ' A-B'
        *             ' A'
        PW/KW-BG/A/KR ' A-B, A-C'
        '''

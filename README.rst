################
Plover Stitching
################

Write stitched words like T-H-I-S or define stitched sequences like heh-heh-heh

Usage
=====

Stitched Fingerspelling
-----------------------

``{:stitch:letter:delimiter?}``

-  **letter**: the letter or word to fingerspell
-  **delimiter** *(optional)*: the character or word to join stitched letters with, *defaults to -*

Examples
^^^^^^^^

- Stitched capital letter alphabet

  - {:stitch:A}{:stitch:B} → A-B

- Joining repeated words

  - {:stitch:ha} → ha
  - {:stitch:ha}{:stitch:ha}{:stitch:ha} → ha-ha-ha

- Custom delimiter

  - {:stitch:lol:o} → lol
  - {:stitch:lol:o}{:stitch:lol:o}{:stitch:lol:o} → lololololol


Stitch Last Words
-----------------

``{:stitch_last_word:count?:delimiter?}``

- **count** *(optional)*: number of previous words to stitch, *defaults to 1*
- **delimiter** *(optional)*: the character or word to join stitched letters with, *defaults to -*

Examples
^^^^^^^^

- Stitch last word

  - this is a test{:stitch_last_word} → this is a t-e-s-t

- Stitch last 2 words

  - my name is John Doe{:stitch_last_word:2} → my name is J-o-h-n D-o-e

- Stitch last word with custom delimiter

  - I'm feeling fabulous{:stitch_last_word:1:✨} → I'm feeling f✨a✨b✨u✨l✨o✨u✨s

Fingerspelling Alphabet
=======================

Here is a fingerspelling dictionary so that you can stitch in capital letters, like when someone is spelling out a name:

.. code:: json

    {
        "A*FPLT": "{:stitch:A}",
        "PW*FPLT": "{:stitch:B}",
        "KR*FPLT": "{:stitch:C}",
        "TK*FPLT": "{:stitch:D}",
        "*EFPLT": "{:stitch:E}",
        "TP*FPLT": "{:stitch:F}",
        "TKPW*FPLT": "{:stitch:G}",
        "H*FPLT": "{:stitch:H}",
        "*EUFPLT": "{:stitch:I}",
        "SKWR*FPLT": "{:stitch:J}",
        "K*FPLT": "{:stitch:K}",
        "HR*FPLT": "{:stitch:L}",
        "PH*FPLT": "{:stitch:M}",
        "TPH*FPLT": "{:stitch:N}",
        "O*FPLT": "{:stitch:O}",
        "P*FPLT": "{:stitch:P}",
        "KW*FPLT": "{:stitch:Q}",
        "R*FPLT": "{:stitch:R}",
        "S*FPLT": "{:stitch:S}",
        "T*FPLT": "{:stitch:T}",
        "*UFPLT": "{:stitch:U}",
        "SR*FPLT": "{:stitch:V}",
        "W*FPLT": "{:stitch:W}",
        "KP*FPLT": "{:stitch:X}",
        "KWR*FPLT": "{:stitch:Y}",
        "STK*FPLT": "{:stitch:Z}",
        "STKPW*FPLT": "{:stitch:Z}"
    }

# हिन्दिक

A repository containing devnagri/hindi transliteration of words in English and
possibly other languages.

The repository would be composed of text files with lines like:

example: इग्ज़ाम्पल (उदाहरड़) - Not sure if to use ज़ or झ there.

Syntax: Word phrase in foreign language, followed by colon, followed by
word/phrase in Hindi, followed by optional meaning of foreign word in Hindi in
parenthesis, followed by optional - and comments.

## Appraoch

Currently I am using [cmudict](https://github.com/cmusphinx/cmudict), which
lists English pronounciation code for some 40-50K words. I am [mapping those
codes to Devnagri](https://github.com/amitu/hindic/blob/master/cmu.py#L25-L68).

## Result so far

Look at [the gist](https://gist.github.com/amitu/47e8438321d0b9e4b3cd) which
shows the conversion of 1000 most frequently used words in English language. It
is only 70-80% accurate so far. Even the accuracy rate is not known, as I am not
that great in English pronunciation myself.

## Help Me Please!

Fork the [gist](https://gist.github.com/amitu/47e8438321d0b9e4b3cd), and correct
it, and send me a mail. Or may be just mark the lines you think are wrong.

Any help with fixing cmu.py is highly appreciated too.

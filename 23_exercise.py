"""Consider the popular Scrabble game. Scrabble is a word game in which
players score points by placing tiles, each bearing a single letter, onto a
game board divided into a 15x15 grid of squares. The tiles must form words
that, in crossword fashion, read left to right in rows or downward in
columns, and be included in a standard dictionary or lexicon.
The combined words are scored, and the game is won by the player who in
total (in all moves) scores more points than each of the opponents. The
number of points is calculated based on the letters in each word. Each letter
has a specific, fixed point value.
Below are the scores for the English version:
• blank tile - O pkt (usually two in a set)
• EAIONRTLSU -1 pkt
• DG - 2 pkt
• BCMP - 3 pkt
• FHVWY - 4 pkt
• K - 5 pkt
• JX - 8 pkt
• QZ -10 pkt
Implement a function called score( ) that returns a result for one word. We
assume that the
given word is grammatically correct. We can represent a blank tile for
simplicity as a space character ‘’.
Tip: We can use the built-in collections module and the ChainMap
class.
"""
from collections import ChainMap

english_scoreboard = {
    "": 0,
    "EAIONTLSU": 1,
    "DG": 2,
    "BCMP": 3,
    "FHVWY": 4,
    "K": 5,
    "JX": 8,
    "QZ": 10
}


def score(word):
    scores = ChainMap(*[dict.fromkeys(letter, score) for letter, score in english_scoreboard.items()])

    return sum([scores[letter.upper()] for letter in word])


print(score("python"))

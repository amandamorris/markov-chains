from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    txt_string = open(file_path).read()

    return txt_string


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    # your code goes here
    words = text_string.split()
    for index in range(0, len(words) - 2):
        bigram = (words[index], words[index + 1])
        chains.setdefault(bigram, [])
        chains[bigram].append(words[index + 2])

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    text = choice(chains.keys())
    sentence = text[0] + " " + text[1]

#    for i in range(10):
    while True:
        # your code goes here
        try:
            follow_word = choice(chains[text])
        except Exception:
            return sentence
        next_bigram = (text[1], follow_word)
        text = next_bigram
        sentence += " " + follow_word
    return sentence

input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)
#print input_text

# Get a Markov chain
chains = make_chains(input_text)
#print chains
# # Produce random text
random_text = make_text(chains)
print random_text

# print random_text

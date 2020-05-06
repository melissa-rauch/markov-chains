"""Generate Markov text from text files."""

from random import choice

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    given_file = open(file_path)
    
    text_string = given_file.read()
                                #.replace("\n"," ")
    #using \n gets rid of the empty space at the end of the line of text
    return(text_string)

# open_and_read_file("green-eggs.txt")

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    

    # your code goes here
    words = text_string.split()
    #loop over the list to retrieve words at correct indices
    for i in range(len(words) -2):
        #assign words at index i and index i+1 to a touple
        word_pairs = (words[i], words[i+1])
        #assign following word to key
        single_word = words[i+2]
        #created a list to hold values associated with Key touples
        followers = chains.get(word_pairs, [])
        # chains[word_pairs] = single_word
        followers.append(single_word)

        chains[word_pairs] = followers

    print(chains)

    # return chains

   
    # return chains
make_chains(open_and_read_file("green-eggs.txt"))

# def make_text(chains):
#     """Return text from chains."""

#     words = []

#     # your code goes here

#     return " ".join(words)


# input_path = "green-eggs.txt"

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print(random_text)

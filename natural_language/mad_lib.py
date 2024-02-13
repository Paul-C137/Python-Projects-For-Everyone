import nltk
import random

# Download the necessary NLTK data (run only once)
# This saves the data in an OS dependent location for the NLTK
# module to use.
# A good way to do this is to run the two lines below in your 
# Python interpreter.
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

def replace_nouns_with_placeholders(text):
    '''This function takes some text as input, assigns parts of speech,
    and replaces half of them with a placeholder.'''
    # Tokenize the text into words
    words = nltk.word_tokenize(text)
    
    # Tag the words with their parts of speech
    tagged_words = nltk.pos_tag(words)
    # The key to understanding the rest of the code is seeing the list
    # of tagged words so, we print it for debugging.
    print(tagged_words)
    
    # Create a list to store modified words
    modified_words = []
    
    # Count the number of nouns
    # This one line of code uses something called a list comprehension.
    # The commented code below is the "for loop" way of doing the same thing.
    num_nouns = sum(1 for _, pos in tagged_words if pos.startswith('N'))

    # Uncomment this code if you don't like list comprehensions
    # Initialize a counter for the number of nouns
    #num_nouns = 0

    # Iterate over each tuple (word, pos) in the tagged_words list
    #for word, pos in tagged_words:
    # Check if the part of speech (pos) starts with 'N', indicating a noun
        #if pos.startswith('N'):
        # If it does, increment the counter by 1
            #num_nouns += 1
    
    # Set a limit for the number of nouns to replace
    num_to_replace = num_nouns // 2
    
    # Iterate over the tagged words
    # This for loop is looping across each tuple in a list and assigning
    # making the 'word' and 'pos' available for each item in the list.
    # Very cool!
    for word, pos in tagged_words:
        # Replace nouns with placeholders randomly
        # All three conditions must be true.  The random.random() function
        # returns a value between 0.0 and 1.0 if you don't provide any 
        # start and stop arguments.  By placing a "random" check in here, 
        # we can tell Python to convert about 50% of the nouns to blanks.
        # For a different percentage, just change it to ".6", for example.
        if pos.startswith('N') and num_to_replace > 0 and random.random() < 0.5:
            modified_words.append('__(NOUN)__')
            num_to_replace -= 1
        else:
            modified_words.append(word)
    
    # Join the modified words back into a string
    modified_text = ' '.join(modified_words)
    
    return modified_text

# Open the file containing the text
file_path = 'madlib_text.txt'  # Replace with the path to your file
with open(file_path, 'r') as file:
    text = file.read()

# Replace half of the nouns with placeholders
modified_text = replace_nouns_with_placeholders(text)

# Print the modified text
print(modified_text)

#!usr/bin/python3

'''P.LACK | lackhack.tech
   Demonstrating three methods for formatting output in Python and how
   to define a function that requires arguments.'''

def print_with_parameters(greeting, subject, verb):
   '''This function uses primarily multiple parameters to print the 
      sentence.  Each comma will represent a space in the output.'''
   print(greeting, subject + "!", "Let's", verb, "Python!")

def print_with_concatenation(greeting, subject, verb):
   '''This function uses string concatenation.  Notice how I have to include
      all of my white spacing inside my strings.'''
   print(greeting + " " + subject + "!" + "  Let's " + verb + " Python!")

def print_with_fstring(greeting, subject, verb):
   '''This function uses and "fstring" to format the output.  Notice how
      much simpler and readable it is to use.  It's faster to type, too.'''
   print(f"{greeting} {subject}! Let's {verb} Python!")

# Test the functions
def main():
   greeting = "Good morning"
   subject = "class"
   verb = "learn"

   print_with_parameters(greeting, subject, verb)
   print_with_concatenation(greeting, subject, verb)
   print_with_fstring(greeting, subject, verb)

# Run the program
if __name__ == "__main__":
   main()
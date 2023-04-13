#!/usr/bin/python3

'''lackhack.tech | Paul Lack
   Word search example using the input() function, 
   opening a file, and formatting output with an fstring.
   There are many ways this program could be improved:
   1. Account for user typing wrongly formatted book title.
   2. Use try/except construction to catch exceptions.
   3. Allow user to do multiple searches.
   4. Display a menu of available books for the user.
   5. Allow user to search all books in the library.
   6. Allow user to replace the searched term with another word.
   7. Make searched terms disregard capitalization.
   8. And many more...'''

def main():
    
    count = 0
    book = input("What book would you like to search? (moby_dick, etc.)  ")
    term = input(f"What word or phrase would you like to search for?  ")
    with open(f"book_files/{book}.txt", "r") as book_file:
        for line in book_file:
            if term in line:
                count += 1
    print(f'"{term}" appears {count} times in the book {book}.')

if __name__ == "__main__":
    main()

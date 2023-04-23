# create an empty list to work with
book_list = ['Stranger in a Strange Land', 'A Canticle for Liebowitz']
# print the current list for the user to see
print(f"Your library contains the following books:")
print(book_list)
# prompt the user to add a title
title = input("Enter the title of the book you wish to add: ")
# use the list.append() method to add the title to the list
book_list.append(title)
# print the list again for the user.
print(f"Your library contains the following books:")
print(book_list)
# prompt the user to remove a title
title = input("Enter the title of the book you wish to remove.")



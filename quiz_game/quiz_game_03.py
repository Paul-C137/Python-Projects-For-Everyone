import random

def get_trivia():
    with open('trivia.txt') as question_file:
        trivia_questions = question_file.readlines()
    return trivia_questions

def show_menu():
   print("Welcome to the Friends Trivia Quiz!")
   print("Type 'q' to quit at any time.")
   print()

def ask_questions():
    for i in range(5):
        trivia_questions = get_trivia()
        question = dict(random.choice(trivia_questions))
        print(question["question"])
        user_answer = input("Your answer: ")

        if user_answer.lower() == 'q':
            break

        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
            trivia_questions.remove(question)
        else:
            print("Incorrect! The correct answer is:", question["answer"])
            trivia_questions.remove(question)

def main():
   global score
   score = 0
   show_menu()
   ask_questions()

   if score > 0:
       print("Quiz ended. Your score:", score)
   else:
       print("Quiz ended. You did not answer any questions.")

if __name__ == "__main__":
   main()
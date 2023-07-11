import random

trivia_questions = [
   {
       "question": "What is the name of Ross and Monica's dog?",
       "answer": "Chi-Chi"
   },
   {
       "question": "What is Joey's catchphrase?",
       "answer": "How you doin'?"
   },
   {
       "question": "What is the name of Phoebe's most popular song?",
       "answer": "Smelly Cat"
   },
   {
       "question": "What is Chandler's job?",
       "answer": "He is a transponster (just kidding! He works in statistical analysis and data reconfiguration)."
   },
   {
       "question": "What is the name of Ross' second wife?",
       "answer": "Emily"
   },
   {
       "question": "What is the name of Joey's stuffed penguin?",
       "answer": "Hugsy"
   },
   {
       "question": "What is the name of the coffee shop where the friends often hang out?",
       "answer": "Central Perk"
   },
   {
       "question": "Which two characters got married in Las Vegas?",
       "answer": "Ross and Rachel"
   },
   {
       "question": "What is the name of Monica and Chandler's twins?",
       "answer": "Erica and Jack"
   },
   {
       "question": "What is Phoebe's sister's name?",
       "answer": "Ursula"
   }
]

def show_menu():
   print("Welcome to the Friends Trivia Quiz!")
   print("Type 'q' to quit at any time.")
   print()

def ask_questions():
    for i in range(5):
        question = random.choice(trivia_questions)
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
def welcome_player():
    """
    Display welcome message, store user name and return greeting
    """


print(
    """
Welcome to my project. This project is for education purposes only.
I hope you will find this quiz fun and interesting.
This quiz contains 15 simple questions
You will answer all the questions by typing A, B, C, or D.
Your answer will not be case-sensitive.
Python will ensure that your answer is accepted
whether you use uppercase or lowercase.
Let's start
    """
)

name = input("How do you want me to call you? ")
name = name.capitalize()
name = name.strip()
while len(name) == 0:
    print(" ")
    print("Sorry i need to know what is your name")
    print(" ")
    name = input("How do you want me to call you? ")
    name = name.capitalize()
    name = name.strip()
else:
    print("Okay " + name + " " "Let's start! :) ")
    print(" ")

questions = {
    "What is Pyhon?": "A",
    "Who created Python?": "C",
    "What year Python was created?": "B",
    "What is Python used for?": "D",
    "Why is paython one of the most popular programming languages?": "B",
    "How do we call @ symbol in Python?": "C",
    "True or False are what data type in Python? ": "A",
    "What is the correct way to create a function in Python?": "D",
    "What is the best web framework for Python?": "D",
    "What is the correct file extension for Python files?": "A",
    "Which statement is used to stop a loop": "B",
    "What was inspration for Python name?": "C",
    "What signifies the end of a statement block or suite in Python?": "D",
    "Which of the following is not a valid data type in python?": "C",
    "Which line of code will add a new element to the end of the list": "A",
}


options = [
    ["A. Programming language", "B. Music genre", "C. Website", "D. Food"],
    ["A. Tesla", "B. Gates", "C. Guido van Rossum", "D. Edison"],
    ["A. 1865", "B. 1991", "C. 2015", "D. 2022"],
    [
        "A. Web Development",
        "B. AI and machine learning",
        "C. Data analytics",
        "D. All of the above",
    ],
    [
        "A. Unnecessarily complicated",
        "B. Powerful yet easy to learn",
        "C. One of the oldest programming languages",
        "D. it's not popular at all",
    ],
    ["A. At", "B. Monkey", "C. Decorator ", "D. Assignment Operator"],
    ["A. Boolean", "B. Integers", "C. Array", "D. Floats"],
    ["A. var", "B. let", "C. int", "D. def"],
    ["A. Laravel", "B. Swift", "C. NET", "D. Django"],
    ["A. py", "B. php", "C. js", "D. json"],
    ["A. stop", "B. brake", "C. exit", "D. pass"],
    [
        "A. Snakes on the plane",
        "B. Medusa",
        "C. British comedy troupe",
        "D. Snake Island",
    ],
    [
        "A. Comment",
        "B. End",
        "C. }",
        "D. A line that is indented less than the previous line",
    ],
    ["A. Int", "B. Float", "C. Double", "D. Str"],
    [
        "A. append().",
        "B. pop().",
        "C. sort().",
        "D. clear().",
    ],
]


def start_game():
    """
    Starting point

    """
    guesses = []
    correct_guesses = 0
    question_num = 1

    """
    Listing questions and options

    """

    for key in questions:
        print("")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        """
        Capturing user input and checking the answer

        """
        print(" ")
        guess = input("So " + name + " what is your answer? ")
        guess = guess.upper()
        guess = guess.strip()
        print(" ")
        while len(guess) == 0:
            print("Sorry answer can't be empty")
            print(" ")
            guess = input("So " + name + " what is your answer? ")
            guess = guess.upper()
            guess = guess.strip()
        else:
            lock = input(
                "Would you like to lock that answer? " + name + " (Yes or No) "
            )
            lock = lock.upper()

        if lock == "NO":
            print(" ")
            guess = input("What is your answer? " + name + " ")
            guess = guess.upper()
            guesses.append(guess)
        else:
            lock == "YES"
            print(" ")
            print("Great, your answer is locked.")
            guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print(" ")
        print("And that is correct answer! Congratulations")
        return 1
    else:
        print(" ")
        print("Unfortunately, that is not the correct answer.")
        print(" ")
        print("You lock " + guess + " And the correct answer is " + answer)
        print(" ")
        print("Game Over")
        print(" ")
        play_again()


def display_score(correct_guesses, guesses):
    score = int((correct_guesses / len(questions)))
    print("Those are all 15 questions, congratulations you won a milon euros")
    print(" ")
    play_again()


def play_again():
    play = input("Would you like to play again? (Yes or No) ")
    play = play.upper()
    if play == "YES":
        start_game()
    else:
        print("Okay " + name + " Thank you for playing")
        quit()


welcome_player()

start_game()

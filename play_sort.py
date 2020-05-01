# 23.04.2020
# Quiz
# functions, files and errors

import sys
import pickle

def new_record(name, score):
    score = str(score)
    new = name + "*" + score + "\n"
    return new

def save_records(new):
    file = open("top_sort.txt", "a+", encoding='utf-8')
    file.write(new)
    file.close()

def display():
    file = open("top_sort.txt", "r", encoding='utf-8')
    records = file.readlines()
    top = []
    for line in records:
        line = line.split("*")
        name = line[0]
        score = int(line[1])
        person = (name, score)
        top.append(person)
    
    top_new = sorted(top, key=lambda top: top[1], reverse=True)
    print("\n\tResults of the top five players:")
    for i in top_new[ : 5]:
        print("\n", i, "\n")
    file.close()

def open_file(file_name, mode):
    """Open file"""
    try:
        the_file = open(file_name, mode, encoding='utf-8')
    except IOError as e:
        print("Unable to open file", file_name, "The program is completed\n", e)
        input("\nPress Enter to exit...")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Returns the next line of a game file in a formatted form"""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Returns the next block of data from the game file"""

    category = next_line(the_file)
    question = next_line(the_file)
    points = next_line(the_file)
    if points:
        points = int(points.strip())

    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    
    correct = next_line(the_file).strip()

    explanation = next_line(the_file)
    return category, question, answers, correct, explanation, points

def welcome(title):
    """Greets the player"""
    print("\t\tWelcome to the Quiz game!\n")
    print(f"\t\t{title}\n")

def main():
    trivia_file = open_file("play.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # first block extraction
    category, question, answers, correct, explanation, points = next_block(trivia_file)
    while category:
        # display question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # receiving a response
        answer = input("Your answer: ")

        # response check
        if answer == correct:
            print("\nYes!", end=" ")
            score += points
        else:
            print("\nNo", end=" ")
        print(explanation)
        print("Score:", score, "\n\n")

        # move on to the next question
        category, question, answers, correct, explanation, points = next_block(trivia_file)

    # end of the game
    trivia_file.close()
    print("That was the last question!")   
    print("You scored", score, "points")

    # saving results and displaying the results of other players
    name = input("What's your name?: ")
    new = new_record(name, score)
    save_records(new)
    display()

main()
input("\n\nPress Enter to exit...")
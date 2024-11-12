from flask import Flask
from random import randint

app = Flask(__name__)

number_to_guess = randint(0, 9)

@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>"\
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'></img>"
            

@app.route('/<int:number>')
def guess(number:int):
    if number > number_to_guess:
        return "<h1>Too High!</h1>"\
            "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExeDVueHR2a2Z4dmFhbHVqcXAzeW0zdjVoeTRudzYwdzBueGhyYnl1cyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3og0IG0skAiznZQLde/giphy.gif'></img>"
    if number < number_to_guess:
        return "<h1>Too Low!</h1>"\
            "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3Q1bjUzcTdhd3lrYXkweWQ5bzNkMXhlMmxpMnBzaHlpOTIxNXUyaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/4TmsyEHp9Ksw8rEyR8/giphy.gif'></img>"
    elif number == number_to_guess:
        return "<h1>Hell Yes!</h1>" \
            "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExa216ZTBxNDA2aWtkc2RjMGUwdWRzdGw1Znl2dWlvcWU2amRkYnA4eSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3ov9jZ0V6gOO0oa98Y/giphy.gif'></img>"       


if __name__=="__main__":
    app.run(debug=True)
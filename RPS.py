from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        player_choice = request.form['choice']
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        result = get_result(player_choice, computer_choice)
        return render_template('index.html', player_choice=player_choice, computer_choice=computer_choice, result=result)
    return render_template('index.html')

def get_result(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (
        (player == 'rock' and computer == 'scissors') or
        (player == 'paper' and computer == 'rock') or
        (player == 'scissors' and computer == 'paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

if __name__ == '__main__':
    app.run(debug=True)
import random
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    users_input = request.args.get("users_input : ", " ")
    return (
        """<form action="" method="get">
                <input type="text" name="input">
                <input type="submit" value="Result">
            </form>"""
        + users_input
    )

@app.route("/<int:users_input>")
# Who is the winner
def determine_winner(users_input):
    lst_of_actions = ['ROCK', 'PAPER', 'SCISSOR']
    user_action = users_input.lower()
    modified_lst = []
    for i in lst_of_actions:
        modified_lst.append(i.lower())
    computer_action = random.choice(modified_lst)
    print(f"\nYou choose {user_action}, computer choose {computer_action}.\n")
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == 'rock':
        if computer_action == 'scissor':
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose!.")
    elif user_action == 'paper':
        if computer_action == 'rock':
            print("Paper covers rock! You win!")
        else :
            print("Scissors cuts paper! You lose!.")
    elif user_action == 'scissor':
        if computer_action == 'paper':
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose!.")

# Get the Winner
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def show_index():
    
    return render_template("index.html")

@app.route("/result")
def check_guess():
    rando = random.randint(0, 100)
    print rando

    count = 0

    guess = request.args.get("guess")

    while count < 11:
        if guess != rando:
            count += 1
            if guess > rando:
                return render_template("index.html", 
                                    response='Too high. Try again!',
                                    count=count)
            elif guess < rando:
                return render_template("index.html", 
                                    response='Too low. Try again!',
                                    count=count)
        else:
            return render_template("index.html", 
                                    response='Hooray! You win.',
                                    count=count)

    return render_template("index.html",
                            response='You lose.')


if __name__ == '__main__':

    app.run(debug=True)



###### TESTING CODE ########

from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def show_index():
    
    return render_template("index.html")

@app.route("/result")
def get_random_number():
    rando = random.randint(0, 100)
    print rando

    return render_template("index.html", rando=rando)

if __name__ == '__main__':

    app.run(debug=True)



###### TESTING CODE ########

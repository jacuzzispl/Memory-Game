import random
from flask import Flask, render_template, request, redirect


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        num_list = []
        digit_span = int(request.form.get('dspan'))
        for _ in range(0, digit_span):
            num_list.append(random.randrange(0, 9))
        num_sequence = "".join(map(str, num_list))
        return render_template('game_play.html', num_list=num_list, num_sequence=num_sequence )
    else:
        return render_template('game_home.html')
    
@app.route("/finish", methods=["POST", "GET"])
def finish():
    data = request.get_json()
    print("I too am listening.")
    return data



if __name__ == "__main__":
    app.run(debug=True)
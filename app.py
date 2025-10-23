import random
from flask import Flask, render_template, request, redirect, jsonify


app = Flask(__name__)
def sequence_generator(x):
    num_list = []
    for _ in range(0, x):
        num_list.append(random.randrange(0, 9))
    num_sequence = "".join(map(str, num_list))
    return num_list, num_sequence

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        print("first")
        digit_span = int(request.form.get('dspan'))
        print(digit_span)
        num_list, num_sequence = sequence_generator(digit_span)
        return render_template('game_play.html', num_list=num_list, num_sequence=num_sequence)
    else:
        print("GET")
        return render_template('game_home.html')
    
@app.route("/finish", methods=["POST", "GET"])
def finish():
    print("finish ran")
    data = request.get_json()
    print(data)
    num_list, num_sequence = sequence_generator(data['dspan'])
    print(num_list, num_sequence)
    return jsonify({"num_list": num_list, "num_sequence": num_sequence})



if __name__ == "__main__":
    app.run(debug=True)
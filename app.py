import random
from flask import Flask, render_template, request, redirect


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        if request.form.get("return-button") == "Return":
            return redirect("/")
        num_list = []
        digit_span = int(request.form.get('dspan'))
        for _ in range(0, digit_span):
            num_list.append(random.randrange(0, 9))
        return render_template('game_play.html', num_list=num_list)
    else:
        return render_template('game_home.html')


if __name__ == "__main__":
    app.run(debug=True)
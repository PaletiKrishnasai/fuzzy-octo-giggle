from flask import Flask, render_template, request

app = Flask(__name__)

# Define the correct code
CORRECT_CODE = "1234"


@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    content = None

    if request.method == "POST":
        user_code = request.form["code"]

        if user_code == CORRECT_CODE:
            content = """
            <p>You have been invited for Krishna's Birthday Party on Saturday - August 31. <strong>Location</strong>:<a href="https://maps.app.goo.gl/ZABG3rxzq5pM9mPE6" target="_blank">1003 W Aaron Dr, Apt 9E.</a>.</p>
            """
        else:
            error = "Should you be having this link in the first place?"

    return render_template("index.html", error=error, content=content)


if __name__ == "__main__":
    app.run(debug=True)
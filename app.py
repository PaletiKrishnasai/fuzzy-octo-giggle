from flask import Flask, render_template, request

app = Flask(__name__)

# Define the correct code
CORRECT_CODE_0 = 7408036355 #chandrika
CORRECT_CODE_1=  8147696063 #sandhya
CORRECT_CODE_2=  5822038514 #chaitanya
CORRECT_CODE_3 = 8147696770 #anis
CORRECT_CODE_4 = 8142808453 # apra
CORRECT_CODE_5 = 8148528359 #mega
CORRECT_CODE_6 = 8147693676 #ragh
CORRECT_CODE_7 = 8142807836 #varun
CORRECT_CODE = 7997


@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    content = None

    if request.method == "POST":
        user_code = request.form["code"]

        if int(user_code) == CORRECT_CODE:
            content = """
            <p>You have been invited for Krishna's Birthday Party on Saturday - August 31, 5pm onwards. <strong>Location</strong>:<a href="https://maps.app.goo.gl/ZABG3rxzq5pM9mPE6" target="_blank">1003 W Aaron Dr, Apt 9E.</a>. Agenda: Board Games + Dinner(I mean its food, amateur cooks here :) ) </p>
            """
        elif int(user_code) == CORRECT_CODE_0:
            content = """
            <p>Your house have been invited for Krishna's Birthday Party on Saturday - August 31, 5pm onwards. <strong>Location</strong>:<a href="https://maps.app.goo.gl/ZABG3rxzq5pM9mPE6" target="_blank">1003 W Aaron Dr, Apt 9E.</a>. Agenda: Board Games + Dinner(I mean its food, amateur cooks here :) ) </p>
            """
        elif int(user_code) == CORRECT_CODE_1:
            content = """
            <p>Your house have been invited for Krishna's Birthday Party on Saturday - August 31, 5pm onwards. <strong>Location</strong>:<a href="https://maps.app.goo.gl/ZABG3rxzq5pM9mPE6" target="_blank">1003 W Aaron Dr, Apt 9E.</a>. Agenda: Board Games + Dinner(I mean its food, amateur cooks here:) ) </p>
            """
        elif int(user_code) == CORRECT_CODE_2:
            content = """
            <p>You have been invited for Krishna's Birthday Party on Saturday - August 31, 5pm onwards. <strong>Location</strong>:<a href="https://maps.app.goo.gl/ZABG3rxzq5pM9mPE6" target="_blank">1003 W Aaron Dr, Apt 9E.</a>. Agenda: Board Games + Dinner(I mean its food, amateur cooks here:) ) </p>
            """
        elif int(user_code) == CORRECT_CODE_3:
            content = """
            <p>You have been invited for Krishna's Birthday Party on Saturday - August 31, 5pm onwards. <strong>Location</strong>:<a href="https://maps.app.goo.gl/ZABG3rxzq5pM9mPE6" target="_blank">1003 W Aaron Dr, Apt 9E.</a>. Agenda: Board Games + Dinner(I mean its food, amateur cooks here:) ) </p>
            """
        elif int(user_code) == CORRECT_CODE_4:
            content = """
            <p>You have been invited for Krishna's Birthday Party on Saturday - August 31, 5pm onwards. <strong>Location</strong>:<a href="https://maps.app.goo.gl/ZABG3rxzq5pM9mPE6" target="_blank">1003 W Aaron Dr, Apt 9E.</a>. Agenda: Board Games + Dinner(I mean its food, amateur cooks here:) ) </p>
            """
        elif int(user_code) == CORRECT_CODE_5:
            content = """
            <p>You have been invited for Krishna's Birthday Party on Saturday - August 31, 5pm onwards. <strong>Location</strong>:<a href="https://maps.app.goo.gl/ZABG3rxzq5pM9mPE6" target="_blank">1003 W Aaron Dr, Apt 9E.</a>. Agenda: Board Games + Dinner(I mean its food, amateur cooks here:) ) </p>
            """
        elif int(user_code) == CORRECT_CODE_6:
            content = """
            <p>You have been invited for Krishna's Birthday Party on Saturday - August 31, 5pm onwards. <strong>Location</strong>:<a href="https://maps.app.goo.gl/ZABG3rxzq5pM9mPE6" target="_blank">1003 W Aaron Dr, Apt 9E.</a>. Agenda: Board Games + Dinner(I mean its food, amateur cooks here:) ) </p>
            """
        elif int(user_code) == CORRECT_CODE_7:
            content = """
            <p>You have been invited for Krishna's Birthday Party on Saturday - August 31, 5pm onwards. <strong>Location</strong>:<a href="https://maps.app.goo.gl/ZABG3rxzq5pM9mPE6" target="_blank">1003 W Aaron Dr, Apt 9E.</a>. Agenda: Board Games + Dinner(I mean its food, amateur cooks here:) ) </p>
            """
        else:
            error = "Should you be having this link in the first place?"

    return render_template("index.html", error=error, content=content)


if __name__ == "__main__":
    app.run(debug=True)
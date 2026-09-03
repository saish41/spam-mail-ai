from flask import (
    Flask,
    render_template,
    request
)

from predict import predict_email


app = Flask(__name__)


@app.route(
    "/",
    methods=["GET", "POST"]
)

def home():

    result = None

    email = ""


    if request.method == "POST":

        email = request.form.get(
            "email",
            ""
        ).strip()


        if email:

            result = predict_email(
                email
            )


    return render_template(

        "index.html",

        result=result,

        email=email

    )


if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )
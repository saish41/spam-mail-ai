import joblib


MODEL_PATH = "model/spam_model.pkl"


model = joblib.load(
    MODEL_PATH
)


def predict_email(email):

    prediction = model.predict(
        [email]
    )[0]

    probabilities = model.predict_proba(
        [email]
    )[0]

    classes = model.classes_

    probability_map = dict(
        zip(
            classes,
            probabilities
        )
    )


    spam_probability = probability_map.get(
        "spam",
        0
    )

    ham_probability = probability_map.get(
        "ham",
        0
    )


    return {

        "prediction": prediction,

        "spam_probability": spam_probability,

        "ham_probability": ham_probability,

        "confidence": max(
            spam_probability,
            ham_probability
        )

    }


if __name__ == "__main__":

    print("\n================================")
    print("       SPAM DETECTION AI")
    print("================================")

    print(
        "\nPaste your email."
    )

    print(
        "Type END on a new line when finished.\n"
    )


    lines = []


    while True:

        line = input()

        if line.strip().upper() == "END":

            break

        lines.append(line)


    email = "\n".join(lines)


    result = predict_email(
        email
    )


    print("\n================================")

    if result["prediction"] == "spam":

        print("🚨 SPAM DETECTED")

    else:

        print("✅ EMAIL APPEARS LEGITIMATE")


    print(
        f"\nConfidence: "
        f"{result['confidence'] * 100:.2f}%"
    )


    print(
        f"Spam probability: "
        f"{result['spam_probability'] * 100:.2f}%"
    )


    print(
        f"Ham probability: "
        f"{result['ham_probability'] * 100:.2f}%"
    )


    print("================================")
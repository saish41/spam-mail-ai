const textarea = document.getElementById("emailInput");

const counter = document.getElementById("counter");

const button = document.getElementById("analyzeButton");


if (textarea && counter) {

    function updateCounter() {

        const length = textarea.value.length;

        counter.textContent =
            `${length.toLocaleString()} characters`;

    }


    textarea.addEventListener(
        "input",
        updateCounter
    );


    updateCounter();

}


if (button) {

    button.addEventListener(
        "click",
        function () {

            if (!textarea.value.trim()) {

                return;

            }

            button.querySelector(
                "span:first-child"
            ).textContent = "ANALYZING...";

        }
    );

}
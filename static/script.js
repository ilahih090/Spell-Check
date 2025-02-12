document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("spellCheckForm");
    const result = document.getElementById("result");

    form.addEventListener("submit", function (event) {
        event.preventDefault();
        
        let inputText = document.getElementById("input_text").value;

        if (inputText.trim() === "") {
            result.innerHTML = "Please enter text!";
            return;
        }

        form.submit(); // Submits the form normally
    });
});
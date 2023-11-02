function addEvent() {
    const button = document.getElementById("my-button");
    const counterDisplay = document.getElementById("counter-display");

    let counter = 0;

    button.addEventListener("click", function () {
        counter++;
        counterDisplay.textContent = counter;
    });
}
addEvent();
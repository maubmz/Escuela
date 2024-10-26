function appendToDisplay(value) {
    document.getElementById("display").value += value;
}

function clearDisplay() {
    document.getElementById("display").value = '';
}

function deleteChar() {
    let display = document.getElementById("display");
    display.value = display.value.slice(0, -1);
}

function calculate() {
    try {
        let display = document.getElementById("display");
        display.value = eval(display.value);
    } catch (error) {
        display.value = "Error";
    }
}

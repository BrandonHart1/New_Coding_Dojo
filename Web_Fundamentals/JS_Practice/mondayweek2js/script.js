var title = document.querySelector("#title")

function display(element) {
    console.log(element);
}

function changeText(element) {
    element.innerText = "You clicked me"
}

function changeBg(element) {
    element.style.backgroundColor = "green"
}

function hoverOver(this) {
    element.style.backgroundColor = "rebeccapurple"
}
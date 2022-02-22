function hideJoin(element) {
    element.style.display = "none"
}

function addLike() {
    var element = document.getElementById("value_like");
    var value = element.innerHTML;

    value++;

    element.innerHTML = value

    console.log(element)
    console.log(value)
    console.log(element.innerHTML)
}


function addLikeTwo() {
    var element = document.getElementById("value_like2");
    var value = element.innerHTML;

    value++;

    element.innerHTML = value

    console.log(element)
    console.log(value)
    console.log(element.innerHTML)
}


function addLikeThree() {
    var element = document.getElementById("value_like3");
    var value = element.innerHTML;

    value++;

    element.innerHTML = value

    console.log(element)
    console.log(value)
    console.log(element.innerHTML)
}


function alertUser(element) {
    console.log(element.value)
    alert(element.value)
}
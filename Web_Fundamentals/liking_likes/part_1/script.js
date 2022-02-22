function addLikes() {
    var element = document.getElementById("likes_section");
    var value = element.innerHTML;

    value++;

    console.log(value)
    document.getElementById("likes_section").innerHTML = value
}


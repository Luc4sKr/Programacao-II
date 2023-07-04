var clicker = document.querySelector("#clicker");
var clicksElement = document.querySelector("#clicks");

var clicks = 0;

clicker.addEventListener("click", function() {
    clicks += 1;
    clicksElement.innerHTML = clicks;
});
var color_picker = document.querySelector("#color-picker");

color_picker.addEventListener("input", function(event) {
    document.body.style.background = event.target.value;
});


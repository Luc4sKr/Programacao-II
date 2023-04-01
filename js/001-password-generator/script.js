const characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const numbers = "0123456789";
const special_digits = "!@#$%&()";
const all_characters = characters + numbers + special_digits;

var generated_password = "";

$(document).ready(() => {

    $("#btn-generate").click((e) => {
        generated_password = generate_password();
        $("#password").text(generated_password);
    });

    $("#btn-copy").click((e) => {
        navigator.clipboard.writeText(generated_password);
    });


    let range = $("#range");
    let password_range = $("#password-range");
    
    range.text(password_range.val());
    password_range.on("input", function () {
        range.html(this.value);
    });
});


function generate_password() {
    let password_range = $("#password-range").val();

    let password = "";
    for (let i = 0; i < password_range; i++) {
        let character = all_characters[random_number(0, all_characters.length - 1)];

        if (characters.includes(character)) {
            if (random_number(0, 1) > 0) {
                character = character.toLowerCase()
            }
        }

        password += character
    }

    return password
}


function random_number(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
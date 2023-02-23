$(document).ready(() => {

    $(window).mousemove((event) => {
        $("#marreta").css({
            top: event.pageY - $("#marreta").outerHeight(true) / 2,
            left: event.pageX - $("#marreta").outerWidth(true) / 2
        });
    });

    $("#cachorro").click(() => {
        $("#cachorro").css({
            top: getRandom(0, $(".game").outerHeight(true) - $("#cachorro").outerHeight(true)),
            left: getRandom(0, $(".game").outerWidth(true) - $("#cachorro").outerWidth(true))
        });
    });

});


function getRandom(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
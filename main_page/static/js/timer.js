$(document).ready(function () {
    function Timeout(fn, interval) {
        var id = setTimeout(fn, interval);
        this.cleared = false;
        this.clear = function () {
            this.cleared = true;
            clearTimeout(id);
        };
    }

    $("#start").on("click", function () {
        milliseconds = 11000;
        try {
            var timer = setTimeout(function () {
                milliseconds -= 1000;
                $("#timer")[0].innerHTML = milliseconds;
            }, 1000);
        } catch (e) {
            console.log(e);
        }
    })
});
$(document).ready(function () {

    $("#fileInput").on("change", function(event) {
        var input = event.target;

        var reader = new FileReader();

        reader.onload = function(e) {
            /* various string parsing */
        };
        reader.readAsText(input.files[0])
    })
});
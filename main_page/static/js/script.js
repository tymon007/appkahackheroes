$(document).ready(function () {
    $("#show_hide_password a").on('click', function (event) {
        event.preventDefault();
        if ($('#show_hide_password input').attr("type") == "text") {
            $('#show_hide_password input').attr('type', 'password');
            $('#show_hide_password i').addClass("fa-eye-slash");
            $('#show_hide_password i').removeClass("fa-eye");
        } else if ($('#show_hide_password input').attr("type") == "password") {
            $('#show_hide_password input').attr('type', 'text');
            $('#show_hide_password i').removeClass("fa-eye-slash");
            $('#show_hide_password i').addClass("fa-eye");
        }
    });

    $("#show_hide_repeat_password a").on('click', function (event) {
        event.preventDefault();
        if ($('#show_hide_repeat_password input').attr("type") == "text") {
            $('#show_hide_repeat_password input').attr('type', 'password');
            $('#show_hide_repeat_password i').addClass("fa-eye-slash");
            $('#show_hide_repeat_password i').removeClass("fa-eye");
        } else if ($('#show_hide_repeat_password input').attr("type") == "password") {
            $('#show_hide_repeat_password input').attr('type', 'text');
            $('#show_hide_repeat_password i').removeClass("fa-eye-slash");
            $('#show_hide_repeat_password i').addClass("fa-eye");
        }
    });

    $("#cancel-log-in").on("click", function () {
        this.parentNode.children[2].click();
    })
});
$(document).ready(function(){
    $('.captcha').click(function () {
        $.getJSON("/refresh_captcha/", function (result) {
            $('#id_captcha').attr('src', result['image_url']);
            $('#id_captcha_0').val(result['hashkey'])
        });
    });
});